---
layout: page
title: Carbon Footprint Calculator
subtitle: An open-source carbon footprint calculator to calculate the impact of your conference
permalink: /carbon-footprint-calculator/
---

<div class="carbon-calculator">

  <!-- Introduction -->
  <section class="calculator-hero mb-5">

    <h2>Understand the impact of conference travel</h2>

    <p class="lead">
      Travel is often one of the largest sources of greenhouse gas emissions
      associated with conferences. Understanding how participants travel can
      help organisers measure their environmental footprint and identify
      opportunities for improvement.
    </p>

    <a
      href="https://github.com/ajanes/ecsa-travel-profile-tool"
      class="btn btn-success"
      style="color:white"
      target="_blank"
      rel="noopener">
      View the open-source project
    </a>
  </section>

  <!-- Why use it -->
  <section class="mb-5">
    <h2>Why use a travel carbon calculator?</h2>

    <p>
      A conference can make sustainability commitments, but measuring the
      impact of travel provides valuable evidence about where the largest
      emissions come from.
    </p>

    <div class="calculator-benefits">

      <div class="benefit-item">
        <div>
          <h3>Measure</h3>
          <p>
            Estimate the distance travelled and associated emissions for
            conference participants.
          </p>
        </div>
      </div>

      <div class="benefit-item">
        <div>
          <h3>Compare</h3>
          <p>
            Understand how different transport choices affect the carbon
            footprint of conference travel.
          </p>
        </div>
      </div>

      <div class="benefit-item">
        <div>
          <h3>Learn</h3>
          <p>
            Use real travel data to understand the environmental impact of
            your event.
          </p>
        </div>
      </div>

      <div class="benefit-item">
        <div>
          <h3>Improve</h3>
          <p>
            Use the results to inform future decisions about conference
            locations, travel and sustainability policies.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- How it works -->
  <section class="mb-5">
    <h2>How it works</h2>

    <p>
      The tool is designed around the reality of conference travel. A
      participant may use several modes of transportation before reaching the
      conference destination, so the tool supports journeys with multiple
      legs.
    </p>

    <div class="row g-4 mt-2">

      <div class="col-12 col-lg-4">
        <div class="card h-100 border-0 shadow-sm process-card">
          <div class="card-body p-4">
            <div class="process-number">1</div>

            <h3>Enter the journey</h3>

            <p>
              Participants enter their starting location and the different
              legs of their journey.
            </p>

            <p class="mb-0">
              For example:
              <strong>home → train station → airport → conference city</strong>.
            </p>
          </div>
        </div>
      </div>

      <div class="col-12 col-lg-4">
        <div class="card h-100 border-0 shadow-sm process-card">
          <div class="card-body p-4">
            <div class="process-number">2</div>

            <h3>Choose transport modes</h3>

            <p>
              Each leg can use a different transport mode, allowing the tool
              to represent realistic multi-modal journeys.
            </p>

            <p class="mb-0">
              Distance is calculated from the selected locations.
            </p>
          </div>
        </div>
      </div>

      <div class="col-12 col-lg-4">
        <div class="card h-100 border-0 shadow-sm process-card">
          <div class="card-body p-4">
            <div class="process-number">3</div>

            <h3>Estimate emissions</h3>

            <p>
              The tool calculates the estimated distance and emissions for
              each journey leg and provides a total for the trip.
            </p>

            <p class="mb-0">
              Results can then be used as conference sustainability data.
            </p>
          </div>
        </div>
      </div>

    </div>
  </section>


  <!-- Example journey -->
  <section class="mb-5">
    <h2>Example journey</h2>

    <p>
      A participant does not necessarily travel from their home directly to
      the conference. The calculator can represent journeys involving several
      transport modes.
    </p>

    <div class="journey-example">

      <div class="journey-step">
        <span class="journey-number">1</span>
        <div>
          <strong>Vienna, Austria</strong>
          <small>Departure</small>
        </div>
      </div>

      <div class="journey-transport">
        🚆
        <span>Train</span>
      </div>

      <div class="journey-step">
        <span class="journey-number">2</span>
        <div>
          <strong>Bolzano, Italy</strong>
          <small>Conference destination</small>
        </div>
      </div>

    </div>

    <div class="example-result mt-4">
      <div>
        <span>Distance</span>
        <strong>423.1 km</strong>
      </div>

      <div>
        <span>Estimated emissions</span>
        <strong>15.02 kg CO₂e</strong>
      </div>
    </div>

    <p class="small text-muted mt-3 mb-0">
      The values above illustrate the type of result produced by the tool.
      Actual results depend on the locations, transport modes and configured
      emissions factors.
    </p>
  </section>


  <!-- Features -->
  <section class="mb-5">
    <h2>Features</h2>

    <div class="row g-4 feature-list">

      <div class="col-12 col-md-6 mt-2">
        <div class="feature-item">
          <span>📍</span>
          <div>
            <h3>Live place search</h3>
            <p>
              Search for locations using a live place-search service rather
              than relying on a bundled city database.
            </p>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-6 mt-2">
        <div class="feature-item">
          <span>🛣️</span>
          <div>
            <h3>Multi-leg journeys</h3>
            <p>
              Represent realistic journeys involving several destinations
              and transport modes.
            </p>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-6 mt-2">
        <div class="feature-item">
          <span>⚙️</span>
          <div>
            <h3>Configurable</h3>
            <p>
              Configure the conference destination, transport modes, dates
              and emissions factors through a YAML configuration file.
            </p>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-6 mt-2">
        <div class="feature-item">
          <span>📋</span>
          <div>
            <h3>Study-data export</h3>
            <p>
              Generate a compact representation of a journey that can be
              copied and used as study data.
            </p>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-6 mt-2">
        <div class="feature-item">
          <span>🔓</span>
          <div>
            <h3>Open source</h3>
            <p>
              The complete application is available under the GPL-3.0 license,
              allowing conferences to adapt the tool to their needs.
            </p>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-6 mt-2">
        <div class="feature-item">
          <span>🐳</span>
          <div>
            <h3>Docker support</h3>
            <p>
              The application can be run locally or deployed using Docker and
              Docker Compose.
            </p>
          </div>
        </div>
      </div>

    </div>
  </section>


  <!-- How conferences can use it -->
  <section class="mb-5">
    <h2>How conferences can use the tool</h2>

    <p>
      The calculator can be integrated into the registration process or
      presented as an optional travel-planning tool. The resulting information
      can then support both immediate communication and longer-term
      sustainability planning.
    </p>

    <div class="row g-1 conference-use-cases">

      <div class="col-12 col-lg-6 mt-2">
        <div class="card h-100 border-0 shadow-sm">
          <div class="card-body p-4">


            <h3>During registration</h3>

            <p>
              Invite participants to describe their expected journey when they
              register for the conference.
            </p>

            <p class="mb-0">
              This makes sustainable travel part of the conversation from the
              beginning.
            </p>

          </div>
        </div>
      </div>

      <div class="col-12 col-lg-6 mt-2">
        <div class="card h-100 border-0 shadow-sm">
          <div class="card-body p-4">


            <h3>After the conference</h3>

            <p>
              Aggregate the collected information to understand the overall
              travel profile of your event.
            </p>

            <p class="mb-0">
              Use the results to identify the biggest sources of emissions.
            </p>

          </div>
        </div>
      </div>

      <div class="col-12 col-lg-6 mt-2">
        <div class="card h-100 border-0 shadow-sm">
          <div class="card-body p-4">


            <h3>For future conferences</h3>

            <p>
              Compare results across editions and use the evidence to guide
              future decisions about locations, travel and conference design.
            </p>

            <p class="mb-0">
              Measurement makes improvement possible.
            </p>

          </div>
        </div>
      </div>

    </div>
  </section>


  <!-- Open source -->
  <section class="mb-5">
    <div class="open-source-card">

      <div class="open-source-icon">💚</div>

      <h2>Built to be reused</h2>

      <p>
        This is not a closed conference-specific service. The application is
        open source and can be configured for different conferences,
        destinations, transport modes and emissions factors.
      </p>

      <p>
        Conference organisers and researchers can inspect the implementation,
        adapt it to their needs and contribute improvements back to the
        project.
      </p>

      <div class="d-flex flex-wrap gap-2 mt-4">

        <a
          href="https://github.com/ajanes/ecsa-travel-profile-tool"
          class="btn btn-success"
          style="color:white"
          target="_blank"
          rel="noopener">
          View repository
        </a>

        <span class="license-badge">
          GPL-3.0
        </span>

      </div>

    </div>
  </section>


  <!-- Technical information -->
  <section class="mb-5">
    <h2>Technical information</h2>

    <p>
      The following information is primarily intended for conference
      organisers, developers and researchers who want to deploy or adapt the
      application.
    </p>

    <div class="accordion" id="technicalInformation">

      <!-- Local installation -->
      <div class="accordion-item">
        <h3 class="accordion-header" id="heading-install">
          <button
            class="accordion-button"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapse-install"
            aria-expanded="true"
            aria-controls="collapse-install">
            Run locally
          </button>
        </h3>

        <div
          id="collapse-install"
          class="accordion-collapse collapse show"
          aria-labelledby="heading-install"
          data-bs-parent="#technicalInformation">

          <div class="accordion-body">

            <pre><code>python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py</code></pre>

            <p>
              The application is then available at
              <code>http://localhost:5000</code>.
            </p>

            <p class="mb-2">
              For development with autoreload:
            </p>

            <pre><code>flask --app run.py --debug run</code></pre>

          </div>
        </div>
      </div>


      <!-- Docker -->
      <div class="accordion-item">
        <h3 class="accordion-header" id="heading-docker">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapse-docker"
            aria-expanded="false"
            aria-controls="collapse-docker">
            Run with Docker
          </button>
        </h3>

        <div
          id="collapse-docker"
          class="accordion-collapse collapse"
          aria-labelledby="heading-docker"
          data-bs-parent="#technicalInformation">

          <div class="accordion-body">

            <pre><code>docker compose up --build</code></pre>

          </div>
        </div>
      </div>


      <!-- Configuration -->
      <div class="accordion-item">
        <h3 class="accordion-header" id="heading-config">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapse-config"
            aria-expanded="false"
            aria-controls="collapse-config">
            Configuration
          </button>
        </h3>

        <div
          id="collapse-config"
          class="accordion-collapse collapse"
          aria-labelledby="heading-config"
          data-bs-parent="#technicalInformation">

          <div class="accordion-body">

            <p>
              Edit
              <code>config/travel-profile-tool.yml</code>
              to configure:
            </p>

            <ul>
              <li>Conference name, dates and fixed destination</li>
              <li>Transport modes and emissions factors</li>
              <li>Place-search API settings</li>
            </ul>

          </div>
        </div>
      </div>


      <!-- API -->
      <div class="accordion-item">
        <h3 class="accordion-header" id="heading-api">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapse-api"
            aria-expanded="false"
            aria-controls="collapse-api">
            HTTP API
          </button>
        </h3>

        <div
          id="collapse-api"
          class="accordion-collapse collapse"
          aria-labelledby="heading-api"
          data-bs-parent="#technicalInformation">

          <div class="accordion-body">

            <h4>GET /api/places?q=term</h4>

            <p>
              Returns normalised place suggestions from the configured place
              provider.
            </p>

            <pre><code>{
  "results": [
    {
      "id": "123",
      "label": "Vienna, Austria",
      "type": "city",
      "lat": 48.2082,
      "lon": 16.3738,
      "country": "Austria"
    }
  ]
}</code></pre>


            <h4>POST /api/calculate</h4>

            <p>
              Calculates distances and estimated emissions for a journey.
            </p>

            <pre><code>{
  "segments": [
    {
      "departure": {
        "label": "Vienna, Austria",
        "lat": 48.2082,
        "lon": 16.3738
      },
      "arrival": {
        "label": "Bolzano, Italy",
        "lat": 46.4983,
        "lon": 11.3548
      },
      "transport_mode": "train"
    }
  ]
}</code></pre>


            <h4>GET /api/itinerary?code=...</h4>

            <p>
              Decodes the compact study-data string and reconstructs the
              itinerary together with its estimated totals.
            </p>

          </div>
        </div>
      </div>


      <!-- Study data -->
      <div class="accordion-item">
        <h3 class="accordion-header" id="heading-data">
          <button
            class="accordion-button collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapse-data"
            aria-expanded="false"
            aria-controls="collapse-data">
            Study-data format
          </button>
        </h3>

        <div
          id="collapse-data"
          class="accordion-collapse collapse"
          aria-labelledby="heading-data"
          data-bs-parent="#technicalInformation">

          <div class="accordion-body">

            <p>
              The interface generates a compact representation of a journey,
              for example:
            </p>

            <pre><code>48.2082,16.3738;1,46.4983,11.3548;2,47.3769,8.5417</code></pre>

            <p>
              The first part represents the initial departure:
            </p>

            <pre><code>start_lat,start_lon</code></pre>

            <p>
              Each following leg is represented as:
            </p>

            <pre><code>mode_id,arrival_lat,arrival_lon</code></pre>

            <p>
              All parts are joined with <code>;</code>.
              The <code>mode_id</code> is the 1-based position of the
              transport mode in
              <code>config/travel-profile-tool.yml</code>.
            </p>

          </div>
        </div>
      </div>

    </div>
  </section>


  <!-- Sources -->
  <section class="mb-5">
    <h2>Data and supporting resources</h2>

    <div class="card border-0 shadow-sm">
      <div class="card-body p-4">

        <ul class="mb-0">

          <li>
            Emissions factors:
            <a
              href="https://ourworldindata.org/grapher/carbon-footprint-travel-mode"
              target="_blank"
              rel="noopener">
              Our World in Data – Carbon footprint of travel modes
            </a>
          </li>

          <li>
            Place search:
            <a
              href="https://github.com/komoot/photon"
              target="_blank"
              rel="noopener">
              Photon
            </a>
          </li>

          <li>
            Default place-search service:
            <a
              href="https://photon.komoot.io"
              target="_blank"
              rel="noopener">
              Photon API
            </a>
          </li>

        </ul>

      </div>
    </div>
  </section>

</div>


<style>
  .carbon-calculator {
    color: #2F3A32;
  }

  .calculator-hero {
    padding: 2.5rem;
    background: #F7FAF5;
    border: 1px solid #C9D9CD;
    border-radius: 1.25rem;
  }

  .calculator-icon {
    font-size: 3rem;
    line-height: 1;
  }

  .carbon-calculator h2 {
    color: #2F3A32;
    font-weight: 600;
    margin-bottom: 1rem;
  }

  .carbon-calculator h3 {
    color: #2F3A32;
    font-weight: 600;
  }

  .carbon-calculator h4 {
    color: #2E5F48;
    font-size: 1rem;
    font-weight: 600;
    margin-top: 1.5rem;
  }

  .carbon-calculator .lead {
    color: #4F6055;
  }

  .carbon-calculator .card {
    border-radius: 1rem;
  }

  .calculator-benefits {
    margin-top: 1.5rem;
  }

  .calculator-benefits .card-body {
    padding: 1.75rem;
  }

  .benefit-icon {
    font-size: 2.25rem;
    line-height: 1;
    margin-bottom: 1.25rem;
  }

  .process-card {
    border-top: 4px solid #2E7D5B !important;
  }

  .process-number {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 2.75rem;
    height: 2.75rem;
    margin-bottom: 1.25rem;
    border-radius: 50%;
    background: #E6EFE8;
    color: #2E7D5B;
    font-weight: 700;
    font-size: 1.1rem;
  }

  .journey-example {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    padding: 2rem;
    margin-top: 1.5rem;
    background: #F7FAF5;
    border: 1px solid #C9D9CD;
    border-radius: 1rem;
  }

  .journey-step {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex: 1;
  }

  .journey-number {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 2.25rem;
    height: 2.25rem;
    border-radius: 50%;
    background: #2E7D5B;
    color: white;
    font-weight: 700;
  }

  .journey-step strong,
  .journey-step small {
    display: block;
  }

  .journey-step small {
    margin-top: 0.25rem;
    color: #6B786F;
  }

  .journey-transport {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.25rem;
    color: #2E7D5B;
    font-weight: 600;
  }

  .example-result {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .example-result > div {
    flex: 1;
    min-width: 200px;
    padding: 1.25rem;
    background: #E6EFE8;
    border-radius: 0.75rem;
  }

  .example-result span,
  .example-result strong {
    display: block;
  }

  .example-result span {
    color: #5F6F63;
    margin-bottom: 0.35rem;
  }

  .example-result strong {
    color: #2E5F48;
    font-size: 1.25rem;
  }

  .feature-list {
    margin-top: 1.5rem;
  }

  .feature-item {
    display: flex;
    gap: 1rem;
    height: 100%;
    padding: 1.5rem;
    background: #FAFCFA;
    border: 1px solid #E1E9E2;
    border-radius: 0.9rem;
  }

  .feature-item > span {
    flex-shrink: 0;
    font-size: 1.75rem;
    line-height: 1;
  }

  .feature-item h3 {
    margin-bottom: 0.5rem;
    font-size: 1.15rem;
  }

  .feature-item p {
    margin-bottom: 0;
    color: #5F6F63;
  }

  .conference-use-cases {
    margin-top: 1.5rem;
  }

  .conference-use-cases .card-body {
    padding: 1.75rem;
  }

  .open-source-card {
    padding: 2.5rem;
    background: #E6EFE8;
    border: 1px solid #C9D9CD;
    border-radius: 1.25rem;
  }

  .open-source-icon {
    font-size: 2.75rem;
    margin-bottom: 1rem;
  }

  .license-badge {
    display: inline-flex;
    align-items: center;
    padding: 0.5rem 0.8rem;
    background: #F7FAF5;
    border: 1px solid #C9D9CD;
    border-radius: 0.5rem;
    color: #2E5F48;
    font-family: monospace;
    font-size: 0.9rem;
    font-weight: 600;
  }

  .carbon-calculator .accordion {
    margin-top: 1.5rem;
  }

  .carbon-calculator .accordion-item {
    border-color: #D9E3DB;
  }

  .carbon-calculator .accordion-button {
    color: #2F3A32;
    font-weight: 600;
    background: #FAFCFA;
  }

  .carbon-calculator .accordion-button:not(.collapsed) {
    color: #2E5F48;
    background: #E6EFE8;
    box-shadow: none;
  }

  .carbon-calculator .accordion-button:focus {
    box-shadow: 0 0 0 0.2rem rgba(46, 125, 91, 0.15);
  }

  .carbon-calculator pre {
    padding: 1rem;
    margin: 1rem 0;
    overflow-x: auto;
    background: #26332B;
    border-radius: 0.6rem;
  }

  .carbon-calculator pre code {
    color: #E6EFE8;
    font-size: 0.9rem;
  }

  .carbon-calculator code {
    color: #2E5F48;
  }

  .carbon-calculator a {
    color: #2E7D5B;
  }

  .carbon-calculator a:hover {
    color: #246B4C;
  }

  .carbon-calculator .btn-success {
    background-color: #2E7D5B;
    border-color: #2E7D5B;
  }

  .carbon-calculator .btn-success:hover,
  .carbon-calculator .btn-success:focus {
    background-color: #246B4C;
    border-color: #246B4C;
  }

  .calculator-closing .card {
    background: #E6EFE8;
  }

  .calculator-closing p {
    color: #4F6055;
  }

  @media (max-width: 767.98px) {
    .calculator-hero,
    .open-source-card {
      padding: 1.5rem;
    }

    .journey-example {
      flex-direction: column;
      align-items: stretch;
    }

    .journey-transport {
      align-items: flex-start;
      flex-direction: row;
    }

    .example-result {
      flex-direction: column;
    }

    .carbon-calculator h2 {
      font-size: 1.6rem;
    }
  }
</style>