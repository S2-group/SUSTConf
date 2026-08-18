#!/usr/bin/env python3
"""
ECSA 2026 transport footprint analysis.

Route format in the `text` column:

    lat,lon;MODE,lat,lon;MODE,lat,lon;...

Example:
    55.3997,10.3852;2,55.6867,12.5701;7,48.1371,11.5754;2,46.4983,11.3548

IMPORTANT:
The numeric mode values are NOT 1-9.

According to the supplied HTML, the mapping is:

    2  = bus_coach
    3  = car_diesel
    4  = car_electric
    5  = ferry_foot
    6  = flight_domestic
    7  = flight_international
    8  = metro
    9  = motorbike
    10 = car_petrol
    11 = car_plugin_hybrid
    12 = train
    13 = tram

Emission factors supplied by the user (2022 gCO2e/km):

    Coach / Long-distance bus       27
    Diesel car                     171
    Electric car                    47
    Ferry (foot passenger)          19
    Domestic flight                246
    International flight          148
    Metro / Underground             28
    Motorbike                      114
    Petrol car                     170
    Plug-in hybrid                  68
    Train / National rail           35
    Tram                             29

Empty `text` values are missing travel data, NOT zero emissions.

Outputs:
    metrics_output/
        transport_summary.csv
        transport_legs.csv
        participant_transport_summary.csv
        transport_modes.png
        transport_distance_distribution.png
        transport_emissions_by_mode.png
        transport_distance_vs_emissions.png
        transport_registered_country.png
"""

from pathlib import Path
import math
import re

import pandas as pd
import matplotlib.pyplot as plt


INPUT = Path("ecsa2026-carbon-footprint.xlsx")
OUTPUT_DIR = Path("metrics_output")
OUTPUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# CORRECT MODE MAPPING
# ---------------------------------------------------------------------------
# The HTML has a disabled placeholder first. Therefore:
#
#   option 1 = disabled "Select transport mode"
#   option 2 = bus_coach
#   option 3 = car_diesel
#   ...
#   option 13 = tram
#
MODE_FACTORS = {
    1: {
        "code": "train",
        "name": "Train",
        "factor": 35,
    },
    2: {
        "code": "bus_coach",
        "name": "Coach / Long-distance bus",
        "factor": 27,
    },
    3: {
        "code": "car_diesel",
        "name": "Diesel car",
        "factor": 171,
    },
    4: {
        "code": "car_petrol",
        "name": "Petrol car",
        "factor": 170,
    },
    5: {
        "code": "car_electric",
        "name": "Electric car",
        "factor": 47,
    },
    6: {
        "code": "car_plugin_hybrid",
        "name": "Plug-in hybrid car",
        "factor": 68,
    },
    7: {
        "code": "motorbike",
        "name": "Motorbike",
        "factor": 114,
    },
    8: {
        "code": "flight_domestic",
        "name": "Flight: domestic",
        "factor": 246,
    },
    9: {
        "code": "flight_international",
        "name": "Flight: international",
        "factor": 148,
    },
    11: {
        "code": "ferry_foot",
        "name": "Ferry (foot passenger)",
        "factor": 19,
    },
    12: {
        "code": "tram",
        "name": "Tram",
        "factor": 29,
    },
    13: {
        "code": "metro",
        "name": "Metro / Underground",
        "factor": 28,
    },
}

COORD = r"-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?"

# Example:
#   ;2,46.4983,11.3548
LEG_RE = re.compile(
    rf";\s*(\d+),({COORD})"
)


def parse_coordinate(value):
    lat, lon = value.split(",")
    return float(lat), float(lon)


def parse_route(value):
    """
    Parse an ECSA route.

    Example:
        50.0875,14.4213;2,46.4983,11.3548

    Returns one dictionary per travel leg.
    """
    if pd.isna(value):
        return []

    text = str(value).strip()

    if not text:
        return []

    parts = text.split(";")

    # The first component must be the origin coordinates.
    if not re.fullmatch(COORD, parts[0].strip()):
        return []

    origin_lat, origin_lon = parse_coordinate(
        parts[0].strip()
    )

    legs = []

    for leg_number, component in enumerate(
        parts[1:],
        start=1,
    ):
        component = component.strip()

        # Each component is:
        #     MODE,DESTINATION_LAT,DESTINATION_LON
        match = re.fullmatch(
            rf"(\d+),({COORD})",
            component,
        )

        if not match:
            return []

        mode_code = int(match.group(1))

        destination_lat, destination_lon = parse_coordinate(
            match.group(2)
        )

        legs.append({
            "leg": leg_number,
            "origin_lat": origin_lat,
            "origin_lon": origin_lon,
            "destination_lat": destination_lat,
            "destination_lon": destination_lon,
            "mode_code": mode_code,
        })

        # Next leg starts where this leg ended.
        origin_lat = destination_lat
        origin_lon = destination_lon

    return legs


def haversine_km(lat1, lon1, lat2, lon2):
    """Great-circle distance between two coordinates, in km."""
    earth_radius_km = 6371.0088

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1)
        * math.cos(phi2)
        * math.sin(dlambda / 2) ** 2
    )

    return (
        2
        * earth_radius_km
        * math.asin(math.sqrt(a))
    )


def main():
    if not INPUT.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT.resolve()}"
        )

    df = pd.read_excel(INPUT)

    if "text" not in df.columns:
        raise ValueError(
            "Expected a column named 'text'."
        )

    df = df.copy()

    # Anonymous row number. This is not exported as a person ID.
    df["_participant_number"] = range(
        1,
        len(df) + 1,
    )

    all_legs = []

    empty_count = 0
    invalid_count = 0
    valid_route_count = 0
    unknown_mode_count = 0

    for _, row in df.iterrows():
        value = row["text"]

        # Empty response = missing data.
        if pd.isna(value) or not str(value).strip():
            empty_count += 1
            continue

        legs = parse_route(value)

        if not legs:
            invalid_count += 1
            continue

        valid_route_count += 1

        registered_country = row.get("country")
        countrycode = row.get("countrycode")

        for leg in legs:
            mode_code = leg["mode_code"]
            mode_info = MODE_FACTORS.get(mode_code)

            if mode_info is None:
                unknown_mode_count += 1

                mode_name = (
                    f"Unknown mode {mode_code}"
                )
                factor = None
                mode_slug = None

            else:
                mode_name = mode_info["name"]
                factor = mode_info["factor"]
                mode_slug = mode_info["code"]

            distance_km = haversine_km(
                leg["origin_lat"],
                leg["origin_lon"],
                leg["destination_lat"],
                leg["destination_lon"],
            )

            if factor is not None:
                emissions_kg = (
                    distance_km
                    * factor
                    / 1000
                )
            else:
                emissions_kg = None

            all_legs.append({
                "participant_number": int(
                    row["_participant_number"]
                ),
                "leg": leg["leg"],
                "origin_lat": leg["origin_lat"],
                "origin_lon": leg["origin_lon"],
                "destination_lat": leg["destination_lat"],
                "destination_lon": leg["destination_lon"],
                "mode_code": mode_code,
                "mode_code_name": mode_slug,
                "mode": mode_name,
                "distance_km": distance_km,
                "emission_factor_gco2e_per_km": factor,
                "estimated_emissions_kg_co2e": emissions_kg,
                "registered_countrycode": (
                    None
                    if pd.isna(countrycode)
                    else str(countrycode)
                ),
                "registered_country": (
                    None
                    if pd.isna(registered_country)
                    else str(registered_country)
                ),
            })

            # Carry destination forward to next leg.
            # parse_route already does this, so no need to modify here.

    legs_df = pd.DataFrame(all_legs)

    # -----------------------------------------------------------------------
    # No routes at all
    # -----------------------------------------------------------------------
    if legs_df.empty:
        print("No valid route strings were found.")
        print(
            f"Total registrations: {len(df)}"
        )
        print(
            f"Empty text values: {empty_count}"
        )
        print(
            f"Invalid/non-route values: {invalid_count}"
        )
        return

    # -----------------------------------------------------------------------
    # Participant-level aggregation
    # -----------------------------------------------------------------------
    participant_summary = (
        legs_df.groupby(
            "participant_number",
            as_index=False,
        )
        .agg(
            legs=("leg", "count"),
            total_distance_km=(
                "distance_km",
                "sum",
            ),
            estimated_emissions_kg_co2e=(
                "estimated_emissions_kg_co2e",
                "sum",
            ),
            registered_country=(
                "registered_country",
                "first",
            ),
            registered_countrycode=(
                "registered_countrycode",
                "first",
            ),
        )
    )

    # Main transport mode = mode covering the largest distance
    # for that participant.
    mode_distance = (
        legs_df.groupby(
            [
                "participant_number",
                "mode",
            ],
            as_index=False,
        )["distance_km"]
        .sum()
        .sort_values(
            [
                "participant_number",
                "distance_km",
            ],
            ascending=[
                True,
                False,
            ],
        )
    )

    main_mode = (
        mode_distance
        .drop_duplicates(
            "participant_number"
        )
        .rename(
            columns={
                "mode":
                    "main_transport_mode"
            }
        )
        [
            [
                "participant_number",
                "main_transport_mode",
            ]
        ]
    )

    participant_summary = (
        participant_summary.merge(
            main_mode,
            on="participant_number",
            how="left",
        )
    )

    # -----------------------------------------------------------------------
    # Summary metrics
    # -----------------------------------------------------------------------
    total_registrations = len(df)
    participants_with_route = len(
        participant_summary
    )
    participants_without_route = (
        total_registrations
        - participants_with_route
    )

    total_distance = legs_df[
        "distance_km"
    ].sum()

    total_emissions = legs_df[
        "estimated_emissions_kg_co2e"
    ].sum()

    summary = {
        "total_registrations":
            total_registrations,

        "participants_with_route":
            participants_with_route,

        "participants_without_route":
            participants_without_route,

        "route_coverage_percent":
            round(
                100
                * participants_with_route
                / total_registrations,
                1,
            )
            if total_registrations
            else 0,

        "total_transport_legs":
            len(legs_df),

        "total_distance_km":
            round(
                total_distance,
                1,
            ),

        "total_distance_million_km":
            round(
                total_distance
                / 1_000_000,
                3,
            ),

        "estimated_emissions_kg_co2e":
            round(
                total_emissions,
                1,
            ),

        "estimated_emissions_t_co2e":
            round(
                total_emissions / 1000,
                3,
            ),

        "mean_distance_per_participant_km":
            round(
                participant_summary[
                    "total_distance_km"
                ].mean(),
                1,
            ),

        "median_distance_per_participant_km":
            round(
                participant_summary[
                    "total_distance_km"
                ].median(),
                1,
            ),

        "mean_emissions_per_participant_kg_co2e":
            round(
                participant_summary[
                    "estimated_emissions_kg_co2e"
                ].mean(),
                1,
            ),

        "median_emissions_per_participant_kg_co2e":
            round(
                participant_summary[
                    "estimated_emissions_kg_co2e"
                ].median(),
                1,
            ),

        "empty_text_values":
            empty_count,

        "invalid_non_route_values":
            invalid_count,

        "unknown_mode_codes":
            unknown_mode_count,
    }

    pd.DataFrame(
        [summary]
    ).to_csv(
        OUTPUT_DIR
        / "transport_summary.csv",
        index=False,
    )

    legs_df.to_csv(
        OUTPUT_DIR
        / "transport_legs.csv",
        index=False,
    )

    participant_summary.to_csv(
        OUTPUT_DIR
        / "participant_transport_summary.csv",
        index=False,
    )

    # -----------------------------------------------------------------------
    # Professional sustainability-themed visualisations
    # -----------------------------------------------------------------------

    import numpy as np
    from matplotlib.ticker import FuncFormatter, MaxNLocator

    # -----------------------------------------------------------------------
    # Visual design system
    # -----------------------------------------------------------------------
    # A restrained green palette: deep forest for emphasis, natural greens
    # for data, and warm off-white backgrounds for a polished report feel.
    COLORS = {
        "forest": "#164A3A",
        "deep_green": "#1F6B4F",
        "green": "#3B8D67",
        "sage": "#76A98B",
        "mint": "#B9D9C5",
        "pale_green": "#E8F2EB",
        "cream": "#F7F8F3",
        "ink": "#20312A",
        "muted": "#66756E",
        "grid": "#D9E2DC",
        "white": "#FFFFFF",
        "accent": "#B9853A",  # restrained warm accent for medians/highlights
    }

    MODE_COLORS = [
        COLORS["forest"],
        COLORS["deep_green"],
        COLORS["green"],
        COLORS["sage"],
        "#4F9D78",
        "#6EAF8D",
        "#8ABFA1",
        "#A4CCB4",
        "#C0DCC9",
        "#D2E6D8",
        "#9DBFA9",
        "#5C9676",
    ]

    plt.rcParams.update({
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "font.family": "DejaVu Sans",
        "font.size": 10.5,
        "axes.titlesize": 20,
        "axes.titleweight": "bold",
        "axes.labelsize": 10.5,
        "axes.labelcolor": COLORS["muted"],
        "axes.edgecolor": COLORS["grid"],
        "axes.facecolor": COLORS["cream"],
        "figure.facecolor": COLORS["cream"],
        "text.color": COLORS["ink"],
        "xtick.color": COLORS["muted"],
        "ytick.color": COLORS["muted"],
        "grid.color": COLORS["grid"],
        "grid.linewidth": 0.8,
        "grid.alpha": 0.8,
        "legend.frameon": False,
        "savefig.facecolor": COLORS["cream"],
    })

    def _shorten_label(label, max_chars=28):
        """Wrap long category labels without losing meaning."""
        label = str(label)
        if len(label) <= max_chars:
            return label
        words = label.split()
        lines, current = [], ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if len(candidate) <= max_chars:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return "\n".join(lines)

    def _add_header(fig, title, subtitle=None):
        """Add consistent report-style title/subtitle treatment."""
        fig.text(
            0.075, 0.94, title,
            ha="left", va="top",
            fontsize=20, fontweight="bold",
            color=COLORS["forest"],
        )
        if subtitle:
            fig.text(
                0.075, 0.895, subtitle,
                ha="left", va="top",
                fontsize=10.5,
                color=COLORS["muted"],
            )

    def _add_footer(fig, text):
        fig.text(
            0.075, 0.025, text,
            ha="left", va="bottom",
            fontsize=8.5,
            color=COLORS["muted"],
        )

    def _finish(ax):
        """Apply consistent minimalist axes styling."""
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_color(COLORS["grid"])
        ax.tick_params(axis="both", length=0, pad=6)
        ax.set_axisbelow(True)

    def _save(fig, filename):
        path = OUTPUT_DIR / filename
        fig.savefig(
            path,
            dpi=300,
            bbox_inches="tight",
            facecolor=fig.get_facecolor(),
            edgecolor="none",
            pad_inches=0.18,
        )
        plt.close(fig)

    def _kg_formatter(value, _):
        if abs(value) >= 1000:
            return f"{value / 1000:,.1f} t"
        return f"{value:,.0f}"

    def _km_formatter(value, _):
        if abs(value) >= 1000:
            return f"{value / 1000:,.1f}k"
        return f"{value:,.0f}"

    # -----------------------------------------------------------------------
    # Plot 1 — transport modes
    # -----------------------------------------------------------------------
    mode_counts = (
        legs_df["mode"]
        .value_counts()
        .sort_values()
    )

    labels = [_shorten_label(x) for x in mode_counts.index]
    values = mode_counts.values

    fig, ax = plt.subplots(figsize=(11, 7))
    fig.subplots_adjust(left=0.33, right=0.96, top=0.80, bottom=0.14)

    bars = ax.barh(
        labels,
        values,
        color=MODE_COLORS[:len(values)],
        height=0.62,
        edgecolor="none",
    )

    max_value = max(values) if len(values) else 1
    ax.set_xlim(0, max_value * 1.16)

    for bar, value in zip(bars, values):
        ax.text(
            value + max_value * 0.018,
            bar.get_y() + bar.get_height() / 2,
            f"{value:,}",
            va="center",
            ha="left",
            fontsize=10,
            fontweight="bold",
            color=COLORS["forest"],
        )

    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
    ax.grid(axis="x", linestyle="-", linewidth=0.7)
    ax.set_xlabel("Transport legs")
    _finish(ax)

    _add_header(
        fig,
        "Transport modes used",
        "Number of recorded travel legs by mode · ECSA 2026",
    )
    _add_footer(
        fig,
        "Counts represent transport legs, not unique participants."
    )
    _save(fig, "transport_modes.png")

    # -----------------------------------------------------------------------
    # Plot 2 — participant distance distribution
    # -----------------------------------------------------------------------
    distances = participant_summary["total_distance_km"].dropna()
    median_distance = distances.median()
    mean_distance = distances.mean()

    fig, ax = plt.subplots(figsize=(11, 7))
    fig.subplots_adjust(left=0.10, right=0.96, top=0.80, bottom=0.17)

    # Adaptive bins give better resolution for the actual dataset while
    # preserving the original interpretation of participant-level distance.
    if len(distances) > 1:
        q95 = distances.quantile(0.95)
        upper = max(q95, median_distance * 2, 100)
        bins = np.linspace(0, upper, 18)
        if distances.max() > upper:
            bins = np.append(bins, distances.max())
    else:
        bins = 10

    ax.hist(
        distances,
        bins=bins,
        color=COLORS["green"],
        alpha=0.88,
        edgecolor=COLORS["white"],
        linewidth=1.2,
    )

    ax.axvline(
        median_distance,
        color=COLORS["forest"],
        linestyle="--",
        linewidth=2,
        label=f"Median · {median_distance:,.0f} km",
    )
    ax.axvline(
        mean_distance,
        color=COLORS["accent"],
        linestyle=":",
        linewidth=2,
        label=f"Mean · {mean_distance:,.0f} km",
    )

    ax.xaxis.set_major_formatter(FuncFormatter(_km_formatter))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
    ax.set_xlabel("Total travel distance per participant")
    ax.set_ylabel("Participants")
    ax.grid(axis="y", linestyle="-")
    ax.legend(loc="upper right", ncol=2)
    _finish(ax)

    _add_header(
        fig,
        "How far did participants travel?",
        "Distribution of total route distance per participant · ECSA 2026",
    )
    _add_footer(
        fig,
        "Distance is calculated as great-circle distance between supplied coordinates."
    )
    _save(fig, "transport_distance_distribution.png")

    # -----------------------------------------------------------------------
    # Plot 3 — emissions by mode
    # -----------------------------------------------------------------------
    emissions_by_mode = (
        legs_df.groupby("mode")["estimated_emissions_kg_co2e"]
        .sum()
        .sort_values()
    )

    labels = [_shorten_label(x) for x in emissions_by_mode.index]
    values = emissions_by_mode.values

    fig, ax = plt.subplots(figsize=(11, 7))
    fig.subplots_adjust(left=0.33, right=0.96, top=0.80, bottom=0.14)

    bars = ax.barh(
        labels,
        values,
        color=COLORS["deep_green"],
        height=0.62,
        edgecolor="none",
    )

    # Highlight the largest emitting mode to make the key message obvious.
    if len(bars):
        largest_idx = int(np.argmax(values))
        bars[largest_idx].set_color(COLORS["forest"])

    max_value = max(values) if len(values) else 1
    ax.set_xlim(0, max_value * 1.20)

    for bar, value in zip(bars, values):
        ax.text(
            value + max_value * 0.018,
            bar.get_y() + bar.get_height() / 2,
            f"{value:,.0f} kg",
            va="center",
            ha="left",
            fontsize=9.5,
            fontweight="bold",
            color=COLORS["forest"],
        )

    ax.xaxis.set_major_formatter(FuncFormatter(_kg_formatter))
    ax.grid(axis="x", linestyle="-")
    ax.set_xlabel("Estimated emissions")
    _finish(ax)

    _add_header(
        fig,
        "Where do transport emissions come from?",
        "Estimated CO₂e by transport mode · ECSA 2026",
    )
    _add_footer(
        fig,
        "Estimated as great-circle distance × supplied 2022 emission factor. "
        "Unknown modes are excluded from emissions calculations."
    )
    _save(fig, "transport_emissions_by_mode.png")

    # -----------------------------------------------------------------------
    # Plot 4 — distance vs emissions
    # -----------------------------------------------------------------------
    scatter_df = participant_summary.dropna(
        subset=["total_distance_km", "estimated_emissions_kg_co2e"]
    ).copy()

    fig, ax = plt.subplots(figsize=(10.5, 7.5))
    fig.subplots_adjust(left=0.11, right=0.97, top=0.80, bottom=0.15)

    x = scatter_df["total_distance_km"]
    y = scatter_df["estimated_emissions_kg_co2e"]

    ax.scatter(
        x,
        y,
        s=48,
        alpha=0.62,
        color=COLORS["green"],
        edgecolors=COLORS["white"],
        linewidths=0.8,
    )

    # A trend line is useful as a visual guide, but is explicitly presented
    # as a fitted relationship rather than a causal model.
    if len(scatter_df) >= 2 and x.nunique() >= 2:
        slope, intercept = np.polyfit(x, y, 1)
        x_line = np.linspace(x.min(), x.max(), 100)
        ax.plot(
            x_line,
            slope * x_line + intercept,
            color=COLORS["forest"],
            linewidth=2.2,
            alpha=0.9,
        )

    ax.xaxis.set_major_formatter(FuncFormatter(_km_formatter))
    ax.yaxis.set_major_formatter(FuncFormatter(_kg_formatter))
    ax.set_xlabel("Total travel distance per participant")
    ax.set_ylabel("Estimated travel emissions (kg CO₂e)")
    ax.grid(True, linestyle="-")
    _finish(ax)

    _add_header(
        fig,
        "Distance and emissions move together",
        "Participant-level relationship between travel distance and estimated footprint",
    )
    _add_footer(
        fig,
        "Each point represents one participant with a parsed route. "
        "The line is a visual linear fit, not a causal estimate."
    )
    _save(fig, "transport_distance_vs_emissions.png")

    # -----------------------------------------------------------------------
    # Plot 5 — registered country
    # -----------------------------------------------------------------------
    country_counts = (
        participant_summary["registered_country"]
        .dropna()
        .value_counts()
        .head(20)
        .sort_values()
    )

    if len(country_counts):
        labels = [_shorten_label(x, 24) for x in country_counts.index]
        values = country_counts.values

        fig, ax = plt.subplots(figsize=(11, 8))
        fig.subplots_adjust(left=0.28, right=0.96, top=0.80, bottom=0.14)

        bars = ax.barh(
            labels,
            values,
            color=COLORS["sage"],
            height=0.62,
            edgecolor="none",
        )

        # Stronger emphasis for the largest group.
        if len(bars):
            bars[-1].set_color(COLORS["forest"])

        max_value = max(values) if len(values) else 1
        ax.set_xlim(0, max_value * 1.16)

        for bar, value in zip(bars, values):
            ax.text(
                value + max_value * 0.015,
                bar.get_y() + bar.get_height() / 2,
                f"{value:,}",
                va="center",
                ha="left",
                fontsize=9.5,
                fontweight="bold",
                color=COLORS["forest"],
            )

        ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
        ax.grid(axis="x", linestyle="-")
        ax.set_xlabel("Participants")
        _finish(ax)

        _add_header(
            fig,
            "Participants by registered country",
            "Top 20 registered countries · ECSA 2026",
        )
        _add_footer(
            fig,
            "Registered country is not necessarily the participant's actual travel origin."
        )
        _save(fig, "transport_registered_country.png")

    # -----------------------------------------------------------------------
    # Console report
    # -----------------------------------------------------------------------
    print()
    print(
        "ECSA 2026 transport footprint analysis"
    )
    print("=" * 60)

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print()
    print(
        "Correct mode mapping:"
    )

    for code, info in MODE_FACTORS.items():
        print(
            f"  {code:>2} = "
            f"{info['code']:<22} "
            f"{info['name']:<32} "
            f"{info['factor']} gCO2e/km"
        )

    print()
    print(
        f"Output directory: "
        f"{OUTPUT_DIR.resolve()}"
    )

    print()
    print(
        "IMPORTANT: distances are great-circle distances "
        "between supplied coordinates."
    )

    print(
        "Empty text values are missing travel data, "
        "not zero emissions."
    )

    if unknown_mode_count:
        print(
            f"WARNING: {unknown_mode_count} legs have "
            "unknown mode codes and therefore no emissions "
            "were calculated for those legs."
        )


if __name__ == "__main__":
    main()