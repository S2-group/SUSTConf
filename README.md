# SUSTConf 🌱

**An open-source framework for sustainability-aware scientific conferences.**

SUSTConf helps conference organisers plan, carry out, measure and report sustainability actions — from choosing a venue and catering to travel, waste and digital communication. It brings together a practical checklist, reusable materials created by other conferences, and a shared evidence base of metrics, so every conference doesn't have to start from zero.

🌐 **Website:** https://s2-group.github.io/SUSTConf/
💻 **Repository:** https://github.com/S2-group/SUSTConf

---

## Table of contents

- [Why SUSTConf exists](#why-sustconf-exists)
- [What's in the framework](#whats-in-the-framework)
- [How to use the framework for your conference](#how-to-use-the-framework-for-your-conference)
- [Adopting SUSTConf](#adopting-sustconf)
- [Contributing](#contributing)
- [Running the website locally](#running-the-website-locally)
- [Publishing on GitHub Pages](#publishing-on-github-pages)
- [Repository structure](#repository-structure)
- [Roadmap](#roadmap)
- [Who is behind SUSTConf](#who-is-behind-sustconf)
- [Credits and licence](#credits-and-licence)

---

## Why SUSTConf exists

In-person scientific conferences are essential for sharing knowledge and building collaborations, but they also have a real ecological footprint: long-distance travel, resource consumption for organising and hosting the event, and the waste it produces.

Many organisers want to do better, but the knowledge on *how* is scattered, rarely reused, and seldom measured. SUSTConf aims to change that by:

- giving organisers **actionable strategies** that reduce the environmental footprint of their event;
- making **good practices reusable** across conferences instead of being reinvented each year;
- building **evidence** on which actions actually work, through shared metrics and reports;
- **raising awareness** of sustainability practices within the research community.

SUSTConf started in 2026 with **ECSA** and **ICSA**, through a collaboration between Vrije Universiteit Amsterdam and the Free University of Bozen-Bolzano, and is open to any conference that wants to join.

## What's in the framework

| Component | What it is | Where |
|---|---|---|
| **Checklist** | ~70 sustainability actions in 15 categories (Venue, Food, Conference Material, Travel, Transport, Digital Communication, Attendance, Information, Waste, Staying, Social, Accessibility, Co-location, and more). Can be filled in on the website and exported/imported as XLS or JSON to share with other chairs. | [Framework page](https://s2-group.github.io/SUSTConf/framework/) |
| **Reusable materials** | Ready-to-adapt resources from conferences that already applied them, e.g. a *Sustainability Knowledge Drops* campaign and an open-source travel carbon-footprint calculator. | [Reusable Materials page](https://s2-group.github.io/SUSTConf/reusable-materials/) |
| **Metrics** | An evolving evidence base of measurements shared by adopting conferences (work in progress), such as the ECSA 2026 travel-emissions analysis. | [Metrics page](https://s2-group.github.io/SUSTConf/metrics/) |

## How to use the framework for your conference

SUSTConf follows a simple pipeline that accompanies a conference from planning to reporting:

```
Checklist  →  Reusable materials  →  Actions  →  Metrics  →  Report
```

1. **Start with the checklist** *(before organisation starts)* — the Sustainability Chair and General Chair(s) go through the checklist together, choose which actions fit their conference, and set priorities. Export it to XLS/JSON to share and edit with the other chairs.
2. **Prepare the actions** *(during organisation)* — use the reusable materials to turn the selected actions into concrete activities.
3. **Execute and measure** *(during organisation and the conference)* — carry out the actions and collect the relevant metrics and evidence.
4. **Report and share** *(after the conference)* — write a short sustainability report with the actions taken, results and metrics, and share it with the community so the next conference can learn from it.

You don't need to install anything to use the framework — everything is available on the website.

## Adopting SUSTConf

Are you organising a conference (software engineering, software architecture, or any other field)? You're welcome to use SUSTConf — no permission needed. We'd love it if you:

- **Tell us** you're using it, by opening an issue titled *"Adoption: <Conference name and year>"*, or by contacting the maintainers (see below). Your conference can then be listed on the website.
- **Mention SUSTConf** on your conference's sustainability page.
- **Share back** what you created (materials, templates, tools) and what you measured (metrics, reports), so the framework keeps growing.

## Contributing

SUSTConf is open source and community-driven. Contributions of every size are welcome — you don't need to be a web developer.

### Ways to contribute

- 💡 **Suggest an idea or report a problem** — open an [issue](https://github.com/S2-group/SUSTConf/issues).
- ✅ **Propose a new checklist action** or improve an existing one.
- 📦 **Share a reusable material** your conference created (campaign, template, tool, guideline…).
- 📊 **Share metrics or a sustainability report** from your conference.
- ✏️ **Fix a typo or improve the text** — every page has an "Edit page" button that takes you straight to the file on GitHub.

### Contribution workflow

1. Fork this repository.
2. Create a branch for your change (`git checkout -b add-my-material`).
3. Make your changes and, ideally, [preview them locally](#running-the-website-locally).
4. Open a pull request describing what you changed and why.

For larger changes, please open an issue first so we can discuss it.

### Where things live

- **A new reusable material** → add a Markdown file in `_posts/` named `YYYY-MM-DD-short-title.md`. In the front matter, include the tag `resource` plus a tag describing its type, and credit the authors:

  ```yaml
  ---
  layout: post
  title: My Reusable Material
  subtitle: One sentence on what it helps organisers do
  author: Jane Doe (My University)
  tags:
    - resource
    - campaign          # the material type, shown as a filter on the website
  ---
  ```

  It will appear automatically on the *Reusable Materials* page. Put images in `assets/img/` and downloadable files next to them or in `additional-files/`.
- **Checklist actions** → `assets/data/sustConf-checklist-data.js` (each action has a unique `id` and a `text`, grouped by category).
- **Framework page** → `pages/framework.md` (styles in `assets/css/framework.css`).
- **Metrics** → `pages/metrics.md`; data and analysis scripts in `additional-files/`.
- **Home page** (goal, partners, people) → `index.html`.
- **Site settings** (title, menu, colours) → `_config.yml`.

## Running the website locally

The website is a static site built with [Jekyll](https://jekyllrb.com/).

### Requirements

- **Ruby** 3.x
  - Windows: install [RubyInstaller](https://rubyinstaller.org/) *with DevKit* and run `ridk install` when prompted.
  - macOS: `brew install ruby`
  - Linux: install `ruby-full` and `build-essential` with your package manager.
- **Bundler**: `gem install bundler`
- **Git**

### Steps

```bash
git clone https://github.com/S2-group/SUSTConf.git
cd SUSTConf
bundle install
bundle exec jekyll serve
```

Then open **http://localhost:4000** in your browser. The site rebuilds automatically when you save a file (changes to `_config.yml` need a restart of `jekyll serve`).

## Publishing on GitHub Pages

The site is deployed automatically by the GitHub Actions workflow in `.github/workflows/jekyll.yml` on every push to the `master` branch.

To publish your own copy (for example, a fork for your conference):

1. Fork the repository.
2. In your fork, go to **Settings → Pages** and set **Source** to **GitHub Actions**.
3. Push a change to `master` (or run the workflow manually from the **Actions** tab).
4. Your site will be available at `https://<your-username>.github.io/SUSTConf/`.

## Repository structure

```
├── index.html                 # Home page
├── pages/                     # Framework, Reusable Materials and Metrics pages
├── _posts/                    # Reusable materials (one file per material)
├── assets/
│   ├── css/                   # Styles (framework.css holds SUSTConf-specific styles)
│   ├── data/                  # Checklist data (sustConf-checklist-data.js)
│   └── img/                   # Images
├── additional-files/          # Metrics data and analysis scripts
├── _layouts/, _includes/      # Page templates (from the Beautiful Jekyll theme)
├── _config.yml                # Site configuration
└── .github/workflows/         # Automatic deployment to GitHub Pages
```

## Roadmap

- [x] Framework pipeline and interactive checklist with XLS/JSON export and import
- [x] First reusable materials (sustainability campaign, travel carbon-footprint calculator)
- [x] First metrics from ECSA 2026 (travel emissions)
- [ ] Complete the Metrics section with a shared reporting template
- [ ] Sustainability report template for the "Report and share" step
- [ ] List of conferences adopting SUSTConf on the website
- [ ] More reusable materials contributed by the community
- [ ] Contribution guide (`CONTRIBUTING.md`) and issue templates for adoptions and new materials

Have an idea? [Open an issue](https://github.com/S2-group/SUSTConf/issues).

## Who is behind SUSTConf

**Creators**
- [Patricia Lago](http://patricialago.nl), Vrije Universiteit Amsterdam (Netherlands)
- Vinicius dos Santos, University of São Paulo (Brazil)

**Collaborators**
- Klervie Toczé, Vrije Universiteit Amsterdam (Netherlands)
- Markus Funke, Vrije Universiteit Amsterdam (Netherlands)
- Andrea Janes, Free University of Bozen-Bolzano (Italy)
- Davide Taibi, University of Southern Denmark (Denmark)

SUSTConf was created and founded in the context of **ECSA 2026** (European Conference on Software Architecture). The Sustainability Campaign material credits **IEEE TCSE** seed funding.

**Contact:** open an [issue](https://github.com/S2-group/SUSTConf/issues) or email Patricia Lago (p.lago@vu.nl).

## Credits and licence

This website is built on **[Beautiful Jekyll](https://github.com/daattali/beautiful-jekyll)** by [Dean Attali](https://deanattali.com), used under the MIT License. Thank you, Dean, for making it freely available! The theme's original copyright and licence notice are kept in [`LICENSE`](LICENSE), and the theme's own history is in [`CHANGELOG.md`](CHANGELOG.md).

The [travel carbon-footprint calculator](https://github.com/ajanes/ecsa-travel-profile-tool) is a separate open-source project by Andrea Janes; see its repository for its licence.

The code in this repository is distributed under the MIT License — see [`LICENSE`](LICENSE).
