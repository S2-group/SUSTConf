---
layout: page
title: SUSTConf Framework
subtitle: A Framework for Sustainability-Aware Conferences
permalink: /framework/
wide-content: true
---
<link rel="stylesheet" href="../assets/css/framework.css">
<script src="../assets/data/sustConf-checklist-data.js"></script>
<script src="https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js"></script>

<body>

  <main>

<header class="intro framework-intro">

  <p class="lead">
    The <strong>SUSTConf Framework</strong> is a collection of reusable materials
    that can support conference organizers in planning, implementing, and evaluating
    sustainability actions.
  </p>

  <p>
    The framework is used through a simple pipeline that accompanies the conference
    from the initial planning stage to the post-conference reporting. The
    <strong>checklist is the starting point</strong>: Sustainability Chairs and General
    Chairs use it to identify the actions that are relevant to their conference and
    define what should be done in the following stages.
  </p>

</header>

<section class="framework-pipeline">

  <div class="pipeline-header">
    <span class="pipeline-kicker">HOW TO USE THE FRAMEWORK</span>
    <h2>From planning to sustainability reporting</h2>
    <p>
      Start with the checklist, use the reusable materials provided by the framework to prepare the selected
      actions, execute them throughout the conference lifecycle, collect evidence
      and metrics, and share the results with the community.
    </p>
  </div>

  <div class="pipeline">

    <article class="pipeline-step start-step">
      <div class="step-number">1</div>
      <div class="step-content">
        <span class="step-phase">BEFORE CONFERENCE ORGANIZATION STARTS</span>
        <h3>Start with the checklist</h3>
        <p>
          Sustainability Chairs and General Chairs fill the checklist together.
          They identify which sustainability actions are relevant, decide which
          actions will be adopted, and list the work that needs to be completed
          during organization, during the conference, and after the conference.
        </p>
        <div class="step-callout">
          <strong>Starting point:</strong> the checklist below defines the
          sustainability actions and priorities for the conference.
        </div>
      </div>
    </article>

    <article class="pipeline-step">
      <div class="step-number">2</div>
      <div class="step-content">
        <span class="step-phase">DURING THE ORGANIZATION</span>
        <h3>Prepare the actions</h3>
        <p>
          Sustainability Chairs use the reusable materials provided by the framework
          to design and set up the actions selected in the checklist. The reusable materials
          provide practical support for turning the selected actions into concrete
          organizational activities.
        </p>
      </div>
    </article>

    <article class="pipeline-step">
      <div class="step-number">3</div>
      <div class="step-content">
        <span class="step-phase">DURING ORGANIZATION &amp; DURING THE CONFERENCE</span>
        <h3>Execute and measure</h3>
        <p>
          The selected sustainability actions are executed during the relevant
          stages of the conference lifecycle. Sustainability Chairs collect the
          corresponding metrics and evidence so that the implementation and its
          results can be evaluated.
        </p>
      </div>
    </article>

    <article class="pipeline-step">
      <div class="step-number">4</div>
      <div class="step-content">
        <span class="step-phase">AFTER THE CONFERENCE</span>
        <h3>Report and share</h3>
        <p>
          Sustainability Chairs consolidate the collected information into a
          sustainability report describing the actions implemented, the results
          obtained, and the relevant metrics. The report should be shared with
          the community to support transparency, learning, and reuse in future
          conferences.
        </p>
      </div>
    </article>

  </div>

  <div class="pipeline-footer">
    <div>
      <strong>Checklist → Reusable Materials → Actions → Metrics → Report</strong>
    </div>
    <p>
      The checklist establishes what the conference intends to do; the framework
      reusable materials support how it is done; the pipeline ensures that actions are
      implemented, measured, and reported.
    </p>
  </div>

</section>


<!-- =========================================================
     LEGEND
     ========================================================= -->

<section class="legend">

  <h2>Legend and Rubric</h2>

  <h3>Priority Levels</h3>

  <p>
    Reflects the priority of items for the conference and should
    be defined by the organizers.
  </p>

  <ul>

    <li>
      <strong>Mandatory (M):</strong>
      The Organizing Committee (OC) can only deviate with approval
      from the Steering Committee (SC).
    </li>

    <li>
      <strong>Strongly Recommended (S):</strong>
      The OC may deviate but must provide justification to the SC.
    </li>

    <li>
      <strong>Optional (O):</strong>
      The OC may deviate without needing to justify the decision.
    </li>

  </ul>


  <h3>Status Indicators</h3>

  <p>
    Reflects the current status of an item.
  </p>

  <ul>

    <li>
      <strong>Done (D):</strong>
      Completed; no further action required.
    </li>

    <li>
      <strong>TODO (TD):</strong>
      Requires consideration or additional work.
    </li>

    <li>
      <strong>Rejected (R):</strong>
      Not included for this conference.
    </li>

  </ul>

</section>


<!-- =========================================================
     INSTRUCTIONS
     ========================================================= -->

<section class="instructions">

  <h2>Instructions</h2>

  <p>
    Fill the checklist below by using the legend and rubric
    provided in this document.
  </p>

  <p>
    It is recommended to set up a group discussion with the
    general chairs to identify the actions that are done,
    should be done (TODO), and are rejected (won't be done).
  </p>

  <p>
    Use the <a href="#checklist-controls">Controls</a> to reorder the categories
    so that the most important ones are discussed first, to show a
    <strong>Notes</strong> column, and to work on the checklist offline or share it
    with other chairs: export it to XLS or JSON, edit the file, and import it back
    into this page.
  </p>

</section>


<!-- =========================================================
     CONTROLS (view options, export and import)
     ========================================================= -->

<section class="data-exchange" id="checklist-controls">
  <h2>Controls</h2>
  <p>
    Adjust how the checklist is displayed and exchange it without creating a
    session: export the values currently filled in below, share the file with
    the other chairs, and import the edited file back into this page.
  </p>
  <div class="exchange-card view-card">
    <h3>View</h3>
    <div class="view-options">
      <label class="toggle-option" for="toggle-notes">
        <input type="checkbox" id="toggle-notes">
        Show the <strong>Notes</strong> column
      </label>
      <button type="button" class="exchange-button" id="reset-order">Reset category order</button>
    </div>
    <p class="exchange-hint">
      Use the <strong>↑</strong> and <strong>↓</strong> buttons next to each category
      title (Venue, Food, …) to change the order of the categories and discuss the
      most important ones first.
    </p>
  </div>
  <div class="exchange-grid">
    <div class="exchange-card">
      <h3>Export</h3>
      <p>Download the checklist exactly as it is currently filled in, in the current category order.</p>
      <div class="exchange-actions">
        <button type="button" class="exchange-button" id="export-xlsx">Export to XLS</button>
        <button type="button" class="exchange-button" id="export-json">Export to JSON</button>
      </div>
      <p class="exchange-hint">
        In the spreadsheet, edit the <strong>Selected</strong> (Yes/No),
        <strong>Priority</strong> (M, S, O), <strong>Status</strong> (D, TD, R) and
        <strong>Notes</strong> columns, and the <strong>Order</strong> column of the
        <em>Categories</em> sheet. Keep the <strong>ID</strong> column unchanged so
        each row can be matched when the file is imported.
      </p>
    </div>
    <form class="exchange-card" id="import-form">
      <h3>Import</h3>
      <p>Load an exported file (.xlsx, .xls, .csv or .json) to fill in the checklist.</p>
      <label class="exchange-label" for="import-file">Checklist file</label>
      <input type="file" id="import-file" name="import_file" accept=".xlsx,.xls,.csv,.json,application/json,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,text/csv" required>
      <fieldset class="exchange-mode">
        <legend>Criteria that are not in the file</legend>
        <label><input type="radio" name="import_mode" value="merge" checked> Keep their current values</label>
        <label><input type="radio" name="import_mode" value="replace"> Clear them</label>
      </fieldset>
      <div class="exchange-actions">
        <button type="submit" class="exchange-button primary">Import</button>
        <button type="button" class="exchange-button" id="import-undo" hidden>Undo import</button>
      </div>
      <div id="import-report" class="import-report" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>

<!-- =========================================================
     CHECKLIST
     ========================================================= -->

<div id="checklist" class="notes-hidden"></div>


<!-- =========================================================
     SOURCES
     ========================================================= -->

<section class="sources">

  <h2>Sources and Methodology</h2>


  <div class="methodology">

    <h3>Methodology</h3>

    <p style="justify-content: justify;">
      The SUSTConf Framework was developed by synthesizing sustainability practices and recommendations from
      previous conferences and from the opinions of conference participants. In addition, a survey was conducted
      during <strong>ICSA 2026</strong> to gather the opinions and perspectives of participants regarding
      sustainability practices for conferences. The collected responses were analyzed using thematic analysis to
      identify recurring sustainability themes and potential actions. Based on this analysis, sustainability actions
      were listed and consolidated. Duplicate or substantially overlapping
      actions were removed in order to produce a concise checklist of distinct actions.
    </p>

  </div>


  <div class="references">

    <h3>References</h3>

    <p>
      The framework draws on sustainability information and recommendations published for the following events:
    </p>

    <ol>

      <ul class="sustainability-links">

        <li>
          <a
            href="https://conf.researchr.org/attending/icsa-2026/Sustainability"
            target="_blank"
            rel="noopener"
          >
            Sustainability
          </a>
          <strong>at ICSA ’26</strong>
        </li>


        <li>
          <a
            href="https://conf.researchr.org/attending/icse-2026/Sustainability"
            target="_blank"
            rel="noopener"
          >
            Sustainability
          </a>
          <strong>at ICSE ’26</strong>
        </li>


        <li>
          <a
            href="https://conf.researchr.org/attending/icse-2025/Sustainability"
            target="_blank"
            rel="noopener"
          >
            Sustainability
          </a>
          <strong>at ICSE ’25</strong>
        </li>


        <li>
          <a
            href="https://conf.researchr.org/attending/ecsa-2024/Sustainability"
            target="_blank"
            rel="noopener"
          >
            Sustainability
          </a>
          <strong>at ECSA ’24</strong>
        </li>


        <li>
          <a
            href="https://conf.researchr.org/attending/ict4s-2023/sustainability"
            target="_blank"
            rel="noopener"
          >
            Sustainability
          </a>
          <strong>at ICT4S ’23</strong>
        </li>

      </ul>

    </ol>

  </div>

</section>

  </main>

  <!-- =========================================================
      REUSABLE MATERIAL COUNTS
       =========================================================

      Reusable material posts are Jekyll posts tagged "resource".

      Every additional tag on a reusable material post is treated as
      a reusable material category.

       The category/tag is the same as the checklist criterion ID.

       Example:

         tags:
           - resource
           - food_local

       The checklist criterion:

         id: food_local

      will therefore show the number of matching reusable material posts.
       ========================================================= -->

  <script>

    /*
    * Reusable material counts.
     *
    * Liquid collects all tags used by reusable material posts and counts
    * how many reusable material posts use each tag.
     */

    const resourceCounts = {};

    {% assign resource_posts = site.posts | where_exp: "post", "post.tags contains 'resource'" %}

    {% assign resource_types = "" | split: "" %}


    /*
     * Collect all resource tags, excluding "resource".
     */

    {% for post in resource_posts %}

      {% for tag in post.tags %}

        {% unless tag == "resource" %}

          {% unless resource_types contains tag %}

            {% assign resource_types = resource_types | push: tag %}

          {% endunless %}

        {% endunless %}

      {% endfor %}

    {% endfor %}


    /*
     * Count the resource posts for every tag.
     */

    {% for tag in resource_types %}

      {% assign resource_count = 0 %}

      {% for post in resource_posts %}

        {% if post.tags contains tag %}

          {% assign resource_count = resource_count | plus: 1 %}

        {% endif %}

      {% endfor %}


      resourceCounts[{{ tag | jsonify }}] =
        {{ resource_count }};

    {% endfor %}

  </script>

  <!-- =========================================================
       CHECKLIST JAVASCRIPT
       ========================================================= -->

  <script>

    /*
     * Priority options
     */

    const priorityOptions = [

      {
        value: "",
        label: ""
      },

      {
        value: "M",
        label: "Mandatory (M)"
      },

      {
        value: "S",
        label: "Strongly Recommended (S)"
      },

      {
        value: "O",
        label: "Optional (O)"
      }

    ];


    /*
     * Status options
     */

    const statusOptions = [

      {
        value: "",
        label: ""
      },

      {
        value: "D",
        label: "Done (D)"
      },

      {
        value: "TD",
        label: "TODO (TD)"
      },

      {
        value: "R",
        label: "Rejected (R)"
      }

    ];


    /*
     * Create a select element.
     */

    function createSelect(name, options) {

      const select =
        document.createElement("select");


      select.name =
        name;


      options.forEach(option => {

        const element =
          document.createElement("option");


        element.value =
          option.value;


        element.textContent =
          option.label;


        select.appendChild(
          element
        );

      });


      return select;

    }


    /*
     * Render the complete checklist.
     */

    function renderChecklist() {

      const container =
        document.getElementById("checklist");


      container.innerHTML = "";


      /*
       * Check that the external data file was loaded.
       */

      if (typeof checklist === "undefined") {

        container.innerHTML = `
          <div class="error">
            <strong>Error:</strong>
            The checklist data could not be loaded.
          </div>
        `;


        console.error(
          "The variable 'checklist' was not found. " +
          "Check the path to " +
          "sustConf-checklist-data.js."
        );


        return;

      }


      /*
       * Generate each checklist section.
       */

      Object.entries(checklist).forEach(
        ([sectionName, section]) => {


          const sectionElement =
            document.createElement("section");


          sectionElement.className =
            "checklist-section";


          sectionElement.dataset.section =
            sectionName;


          /*
           * Section heading with the buttons to change the
           * order of the categories.
           */

          const sectionHeader =
            document.createElement("div");


          sectionHeader.className =
            "section-header";


          const heading =
            document.createElement("h2");


          const position =
            document.createElement("span");


          position.className =
            "section-position";


          heading.appendChild(
            position
          );


          heading.appendChild(
            document.createTextNode(sectionName)
          );


          const moveButtons =
            document.createElement("div");


          moveButtons.className =
            "section-move";


          [
            { direction: -1, symbol: "↑", className: "move-section-up", label: "up" },
            { direction: 1, symbol: "↓", className: "move-section-down", label: "down" }
          ].forEach(move => {

            const button =
              document.createElement("button");


            button.type =
              "button";


            button.className =
              move.className;


            button.textContent =
              move.symbol;


            button.title =
              `Move ${sectionName} ${move.label}`;


            button.setAttribute(
              "aria-label",
              `Move ${sectionName} ${move.label}`
            );


            button.addEventListener(
              "click",
              () => moveSection(sectionElement, move.direction, button)
            );


            moveButtons.appendChild(
              button
            );

          });


          sectionHeader.appendChild(
            heading
          );


          sectionHeader.appendChild(
            moveButtons
          );


          sectionElement.appendChild(
            sectionHeader
          );


          /*
           * Table.
           */

          const table =
            document.createElement("table");


          /*
           * Table header.
           */

          const thead =
            document.createElement("thead");


          const headerRow =
            document.createElement("tr");


          /*
           * Checkmark column.
           */

          const checkHeader =
            document.createElement("th");


          checkHeader.textContent =
            "✓";


          checkHeader.className =
            "check-column";


          checkHeader.setAttribute(
            "aria-label",
            "Selected"
          );


          headerRow.appendChild(
            checkHeader
          );


          /*
           * Criterion column.
           */

          const criterionHeader =
            document.createElement("th");


          criterionHeader.textContent =
            "Criterion";


          criterionHeader.className =
            "criterion-column";


          headerRow.appendChild(
            criterionHeader
          );


          /*
           * Priority column.
           */

          const priorityHeader =
            document.createElement("th");


          priorityHeader.textContent =
            "Priority";


          priorityHeader.className =
            "priority-column";


          headerRow.appendChild(
            priorityHeader
          );


          /*
           * Status column.
           */

          const statusHeader =
            document.createElement("th");


          statusHeader.textContent =
            "Status";


          statusHeader.className =
            "status-column";


          headerRow.appendChild(
            statusHeader
          );


          /*
           * Notes column (hidden unless enabled in the Controls).
           */

          const notesHeader =
            document.createElement("th");


          notesHeader.textContent =
            "Notes";


          notesHeader.className =
            "notes-column";


          headerRow.appendChild(
            notesHeader
          );


          /*
           * Reusable Materials column.
           */

          const resourcesHeader =
            document.createElement("th");


          resourcesHeader.textContent =
            "Reusable Materials";


          resourcesHeader.className =
            "resources-column";


          headerRow.appendChild(
            resourcesHeader
          );


          thead.appendChild(
            headerRow
          );


          table.appendChild(
            thead
          );


          /*
           * Table body.
           */

          const tbody =
            document.createElement("tbody");


          section.criteria.forEach(
            criterion => {


              const row =
                document.createElement("tr");


              /*
               * --------------------------------------------------
               * Checkbox
               * --------------------------------------------------
               */

              const checkCell =
                document.createElement("td");


              checkCell.className =
                "check-column";


              const checkbox =
                document.createElement("input");


              checkbox.type =
                "checkbox";


              checkbox.name =
                criterion.id;


              checkbox.id =
                criterion.id;


              checkCell.appendChild(
                checkbox
              );


              /*
               * --------------------------------------------------
               * Criterion
               * --------------------------------------------------
               */

              const criterionCell =
                document.createElement("td");


              const label =
                document.createElement("label");


              label.htmlFor =
                criterion.id;


              label.textContent =
                criterion.text;


              criterionCell.appendChild(
                label
              );


              /*
               * --------------------------------------------------
               * Priority
               * --------------------------------------------------
               */

              const priorityCell =
                document.createElement("td");


              const priority =
                createSelect(
                  `priority_${criterion.id}`,
                  priorityOptions
                );


              priorityCell.appendChild(
                priority
              );


              /*
               * --------------------------------------------------
               * Status
               * --------------------------------------------------
               */

              const statusCell =
                document.createElement("td");


              const status =
                createSelect(
                  `status_${criterion.id}`,
                  statusOptions
                );


              statusCell.appendChild(
                status
              );


              /*
               * --------------------------------------------------
               * Notes
               * --------------------------------------------------
               */

              const notesCell =
                document.createElement("td");


              notesCell.className =
                "notes-column";


              const notes =
                document.createElement("textarea");


              notes.name =
                `notes_${criterion.id}`;


              notes.rows =
                2;


              notes.setAttribute(
                "aria-label",
                `Notes for ${criterion.text}`
              );


              notesCell.appendChild(
                notes
              );


              /*
               * --------------------------------------------------
               * Reusable Materials
               * --------------------------------------------------
               */

              const resourcesCell =
                document.createElement("td");


              resourcesCell.className =
                "resources-column";


              const resourceCount =
                resourceCounts[criterion.id] || 0;


              /*
               * If reusable materials exist, make the number a link.
               *
               * Example:
               *
               *   /reusable-materials/?type=food_local
               *
               * The Reusable Materials page can then use the "type"
               * parameter to filter the reusable materials.
               */

              if (resourceCount > 0) {

                const resourcesLink =
                  document.createElement("a");


                resourcesLink.href =
                  `{{ '/reusable-materials/' | relative_url }}?type=${encodeURIComponent(criterion.id)}`;


                resourcesLink.textContent =
                  resourceCount;


                resourcesLink.className =
                  "resources-count-link";


                resourcesLink.setAttribute(
                  "aria-label",
                  `View ${resourceCount} reusable materials for ${criterion.text}`
                );


                resourcesCell.appendChild(
                  resourcesLink
                );

              } else {

                resourcesCell.textContent =
                  "0";

              }


              /*
               * Add cells to row.
               */

              row.appendChild(
                checkCell
              );


              row.appendChild(
                criterionCell
              );


              row.appendChild(
                priorityCell
              );


              row.appendChild(
                statusCell
              );


              row.appendChild(
                notesCell
              );


              row.appendChild(
                resourcesCell
              );


              /*
               * Add row to table.
               */

              tbody.appendChild(
                row
              );

            }
          );


          table.appendChild(
            tbody
          );


          sectionElement.appendChild(
            table
          );


          container.appendChild(
            sectionElement
          );

        }
      );

    }



    /*
     * =========================================================
     * CATEGORY ORDER AND NOTES COLUMN
     * =========================================================
     */

    function getChecklistContainer() {

      return document.getElementById("checklist");

    }


    function getSectionElements() {

      const container = getChecklistContainer();

      return container
        ? Array.from(container.children).filter(element => element.classList.contains("checklist-section"))
        : [];

    }


    /*
     * Current order of the categories, as shown on the page.
     */

    function getSectionOrder() {

      return getSectionElements().map(element => element.dataset.section);

    }


    function isDefaultOrder() {

      const defaultOrder = Object.keys(checklist);

      return getSectionOrder().every((name, index) => name === defaultOrder[index]);

    }


    /*
     * Update the position numbers and enable/disable the move buttons.
     */

    function updateSectionControls() {

      const sections = getSectionElements();

      sections.forEach((element, index) => {

        const position = element.querySelector(".section-position");
        const up = element.querySelector(".move-section-up");
        const down = element.querySelector(".move-section-down");

        if (position) {
          position.textContent = `${index + 1}.`;
        }

        if (up) {
          up.disabled = index === 0;
        }

        if (down) {
          down.disabled = index === sections.length - 1;
        }

      });

      const reset = document.getElementById("reset-order");

      if (reset) {
        reset.disabled = isDefaultOrder();
      }

    }


    /*
     * Move a category one position up (-1) or down (+1).
     */

    function moveSection(sectionElement, direction, button) {

      const container = getChecklistContainer();

      if (direction < 0) {

        const previous = sectionElement.previousElementSibling;

        if (previous && previous.classList.contains("checklist-section")) {
          container.insertBefore(sectionElement, previous);
        }

      } else {

        const next = sectionElement.nextElementSibling;

        if (next && next.classList.contains("checklist-section")) {
          container.insertBefore(next, sectionElement);
        }

      }

      updateSectionControls();

      /*
       * Keep the keyboard focus on the moved category.
       */

      if (button) {

        const target = button.disabled
          ? sectionElement.querySelector(direction < 0 ? ".move-section-down" : ".move-section-up")
          : button;

        if (target && !target.disabled) {
          target.focus({ preventScroll: true });
        }

      }

      sectionElement.scrollIntoView({ block: "nearest", behavior: "smooth" });

    }


    /*
     * Put the categories in the given order. Categories not listed keep
     * their relative order and are placed after the listed ones.
     */

    function applySectionOrder(order) {

      const container = getChecklistContainer();

      const byName = new Map(getSectionElements().map(element => [element.dataset.section, element]));

      const placed = new Set();

      order.forEach(name => {

        const element = byName.get(name);

        if (element && !placed.has(name)) {
          container.appendChild(element);
          placed.add(name);
        }

      });

      byName.forEach((element, name) => {

        if (!placed.has(name)) {
          container.appendChild(element);
        }

      });

      updateSectionControls();

    }


    function areNotesVisible() {

      const container = getChecklistContainer();

      return Boolean(container) && !container.classList.contains("notes-hidden");

    }


    function setNotesVisible(visible) {

      const container = getChecklistContainer();

      if (container) {
        container.classList.toggle("notes-hidden", !visible);
      }

      const toggle = document.getElementById("toggle-notes");

      if (toggle) {
        toggle.checked = visible;
      }

    }


    /*
     * =========================================================
     * EXPORT / IMPORT
     * =========================================================
     *
     * The checklist can be exchanged as a spreadsheet (XLSX, via
     * SheetJS) or as JSON. Both formats contain one entry per
     * criterion, in the current category order:
     *
     *   Section | ID | Criterion | Selected | Priority | Status | Notes
     *
     * The category order is stored in the "Categories" sheet of the
     * spreadsheet (Order | Category) and in "sectionOrder" in JSON.
     *
     * Rows are matched on import by ID (falling back to the
     * criterion text), so the ID column must not be changed.
     */

    const EXCHANGE_FORMAT = "sustconf-checklist";

    const EXCHANGE_VERSION = 2;

    const EXPORT_COLUMNS = [
      "Section",
      "ID",
      "Criterion",
      "Selected",
      "Priority",
      "Status",
      "Notes"
    ];

    let lastImportSnapshot = null;


    /*
     * Controls of a criterion row.
     */

    function getControls(id) {

      return {
        checkbox: document.getElementById(id),
        priority: document.querySelector(`select[name="priority_${id}"]`),
        status: document.querySelector(`select[name="status_${id}"]`),
        notes: document.querySelector(`textarea[name="notes_${id}"]`)
      };

    }


    /*
     * Read the current checklist values from the page,
     * in the order the categories are displayed.
     */

    function getChecklistState() {

      const items = [];

      getSectionOrder().forEach(sectionName => {

        const section = checklist[sectionName];

        if (!section) {
          return;
        }

        section.criteria.forEach(criterion => {

          const controls = getControls(criterion.id);

          items.push({
            section: sectionName,
            id: criterion.id,
            criterion: criterion.text,
            selected: controls.checkbox ? controls.checkbox.checked : false,
            priority: controls.priority ? controls.priority.value : "",
            status: controls.status ? controls.status.value : "",
            notes: controls.notes ? controls.notes.value : ""
          });

        });

      });

      return items;

    }


    /*
     * Everything needed to restore the page (used by "Undo import").
     */

    function getPageSnapshot() {

      return {
        items: getChecklistState(),
        order: getSectionOrder(),
        showNotes: areNotesVisible()
      };

    }


    /*
     * Write values into one criterion row.
     */

    function setCriterionValues(id, values) {

      const controls = getControls(id);

      if (values.selected !== undefined && controls.checkbox) {
        controls.checkbox.checked = values.selected;
      }

      if (values.priority !== undefined && controls.priority) {
        controls.priority.value = values.priority;
      }

      if (values.status !== undefined && controls.status) {
        controls.status.value = values.status;
      }

      if (values.notes !== undefined && controls.notes) {
        controls.notes.value = values.notes;
      }

    }


    function exportFileName(extension) {

      const today = new Date().toISOString().slice(0, 10);

      return `sustconf-checklist-${today}.${extension}`;

    }


    function downloadBlob(blob, fileName) {

      const url = URL.createObjectURL(blob);

      const link = document.createElement("a");

      link.href = url;
      link.download = fileName;

      document.body.appendChild(link);
      link.click();
      link.remove();

      setTimeout(() => URL.revokeObjectURL(url), 1000);

    }


    /*
     * Export to JSON.
     */

    function exportJson() {

      const data = {
        format: EXCHANGE_FORMAT,
        version: EXCHANGE_VERSION,
        exportedAt: new Date().toISOString(),
        sectionOrder: getSectionOrder(),
        showNotes: areNotesVisible(),
        legend: {
          priority: { M: "Mandatory", S: "Strongly Recommended", O: "Optional" },
          status: { D: "Done", TD: "TODO", R: "Rejected" }
        },
        items: getChecklistState()
      };

      const blob = new Blob(
        [JSON.stringify(data, null, 2)],
        { type: "application/json" }
      );

      downloadBlob(blob, exportFileName("json"));

    }


    /*
     * Export to XLSX (opens in Excel, LibreOffice and Google Sheets).
     */

    function exportXlsx() {

      if (typeof XLSX === "undefined") {

        showImportReport(
          "error",
          "The spreadsheet library could not be loaded. Check your internet connection, or use Export to JSON."
        );

        return;

      }

      const rows = getChecklistState().map(item => ({
        Section: item.section,
        ID: item.id,
        Criterion: item.criterion,
        Selected: item.selected ? "Yes" : "No",
        Priority: item.priority,
        Status: item.status,
        Notes: item.notes
      }));

      const sheet = XLSX.utils.json_to_sheet(rows, { header: EXPORT_COLUMNS });

      sheet["!cols"] = [
        { wch: 22 },
        { wch: 34 },
        { wch: 80 },
        { wch: 10 },
        { wch: 10 },
        { wch: 10 },
        { wch: 60 }
      ];

      sheet["!autofilter"] = {
        ref: XLSX.utils.encode_range({
          s: { r: 0, c: 0 },
          e: { r: rows.length, c: EXPORT_COLUMNS.length - 1 }
        })
      };

      const categories = XLSX.utils.aoa_to_sheet(
        [["Order", "Category"]].concat(
          getSectionOrder().map((name, index) => [index + 1, name])
        )
      );

      categories["!cols"] = [{ wch: 8 }, { wch: 30 }];

      const legend = XLSX.utils.aoa_to_sheet([
        ["Column", "Allowed value", "Meaning"],
        ["Selected", "Yes", "The criterion is selected"],
        ["Selected", "No", "The criterion is not selected"],
        ["Priority", "M", "Mandatory: the OC can only deviate with approval from the SC"],
        ["Priority", "S", "Strongly Recommended: the OC may deviate but must justify it to the SC"],
        ["Priority", "O", "Optional: the OC may deviate without justification"],
        ["Priority", "(empty)", "Not defined yet"],
        ["Status", "D", "Done: completed, no further action required"],
        ["Status", "TD", "TODO: requires consideration or additional work"],
        ["Status", "R", "Rejected: not included for this conference"],
        ["Status", "(empty)", "Not defined yet"],
        ["Notes", "Free text", "Comments, decisions or responsibilities for the criterion"],
        [],
        ["Note", "", "Do not change the ID column: it is used to match rows when importing the file."],
        ["Note", "", "To change the order of the categories, edit the Order column in the Categories sheet."]
      ]);

      legend["!cols"] = [{ wch: 12 }, { wch: 14 }, { wch: 80 }];

      const workbook = XLSX.utils.book_new();

      XLSX.utils.book_append_sheet(workbook, sheet, "Checklist");
      XLSX.utils.book_append_sheet(workbook, categories, "Categories");
      XLSX.utils.book_append_sheet(workbook, legend, "Legend");

      XLSX.writeFile(workbook, exportFileName("xlsx"));

    }


    /*
     * ---------------------------------------------------------
     * Import helpers
     * ---------------------------------------------------------
     */

    function normalizeKey(key) {

      return String(key).trim().toLowerCase().replace(/[^a-z]/g, "");

    }


    function pickField(row, names) {

      for (const key of Object.keys(row)) {

        if (names.includes(normalizeKey(key))) {
          return row[key];
        }

      }

      return undefined;

    }


    /*
     * Accept codes ("M"), labels ("Mandatory (M)") or words ("mandatory").
     * Returns the code, "" for empty, or null if the value is not valid.
     */

    function parseOption(value, options, words) {

      if (value === undefined || value === null) {
        return "";
      }

      const text = String(value).trim();

      if (text === "") {
        return "";
      }

      const upper = text.toUpperCase();

      for (const option of options) {

        if (option.value === "") {
          continue;
        }

        if (upper === option.value || upper === option.label.toUpperCase()) {
          return option.value;
        }

      }

      const code = text.match(/\(([A-Za-z]+)\)/);

      if (code && options.some(option => option.value === code[1].toUpperCase())) {
        return code[1].toUpperCase();
      }

      const simplified = text.toLowerCase().replace(/[^a-z]/g, "");

      for (const [word, optionValue] of Object.entries(words)) {

        if (simplified.startsWith(word)) {
          return optionValue;
        }

      }

      return null;

    }


    function parsePriority(value) {

      return parseOption(value, priorityOptions, {
        mandatory: "M",
        strongly: "S",
        optional: "O"
      });

    }


    function parseStatus(value) {

      return parseOption(value, statusOptions, {
        done: "D",
        todo: "TD",
        rejected: "R"
      });

    }


    function parseSelected(value) {

      if (typeof value === "boolean") {
        return value;
      }

      if (typeof value === "number") {
        return value !== 0;
      }

      const text = String(value === undefined || value === null ? "" : value)
        .trim()
        .toLowerCase();

      if (["yes", "y", "true", "x", "1", "✓", "✔", "checked", "selected", "sim", "ja", "oui", "si", "sí"].includes(text)) {
        return true;
      }

      if (["no", "n", "false", "0", "", "-", "unchecked", "não", "nao", "nein", "non"].includes(text)) {
        return false;
      }

      return null;

    }


    /*
     * Turn the content of a JSON file into rows and settings.
     */

    function parseJsonImport(data) {

      const result = { rows: null, sectionOrder: null, showNotes: undefined };

      if (Array.isArray(data)) {

        result.rows = data;

      } else if (data && Array.isArray(data.items)) {

        result.rows = data.items;

        if (Array.isArray(data.sectionOrder)) {
          result.sectionOrder = data.sectionOrder.map(name => String(name));
        }

        if (typeof data.showNotes === "boolean") {
          result.showNotes = data.showNotes;
        }

      } else if (data && typeof data === "object") {

        /*
         * Also accept a simple map: { "criterion_id": { priority, status, selected, notes } }
         */

        result.rows = Object.entries(data)
          .filter(([, value]) => value && typeof value === "object" && !Array.isArray(value))
          .map(([id, value]) => Object.assign({ id: id }, value));

      } else {

        throw new Error("The JSON file does not contain checklist items.");

      }

      return result;

    }


    /*
     * Read the "Checklist" sheet (or the first sheet) and, if present,
     * the "Categories" sheet with the category order.
     */

    function parseWorkbookImport(buffer) {

      if (typeof XLSX === "undefined") {
        throw new Error("The spreadsheet library could not be loaded. Check your internet connection, or import a JSON file.");
      }

      const workbook = XLSX.read(buffer, { type: "array" });

      const findSheet = name =>
        workbook.SheetNames.find(sheetName => sheetName.trim().toLowerCase() === name);

      const sheetName = findSheet("checklist") || workbook.SheetNames[0];

      if (!sheetName) {
        throw new Error("The spreadsheet does not contain any sheet.");
      }

      const result = {
        rows: XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], { defval: "" }),
        sectionOrder: null,
        showNotes: undefined
      };

      const categoriesName = findSheet("categories");

      if (categoriesName && categoriesName !== sheetName) {

        const categoryRows = XLSX.utils.sheet_to_json(workbook.Sheets[categoriesName], { defval: "" });

        const entries = categoryRows
          .map((row, index) => {

            const name = pickField(row, ["category", "section", "name"]);
            const order = parseFloat(pickField(row, ["order", "position", "priority"]));

            return {
              name: name === undefined ? "" : String(name).trim(),
              order: Number.isFinite(order) ? order : Number.MAX_SAFE_INTEGER,
              index: index
            };

          })
          .filter(entry => entry.name !== "");

        entries.sort((a, b) => a.order - b.order || a.index - b.index);

        if (entries.length > 0) {
          result.sectionOrder = entries.map(entry => entry.name);
        }

      }

      return result;

    }


    function readFile(file) {

      return new Promise((resolve, reject) => {

        const reader = new FileReader();

        reader.onload = () => resolve(reader.result);
        reader.onerror = () => reject(new Error("The file could not be read."));

        if (/\.json$/i.test(file.name) || file.type === "application/json") {
          reader.readAsText(file);
        } else {
          reader.readAsArrayBuffer(file);
        }

      });

    }


    /*
     * Apply an imported file to the checklist.
     */

    function applyImport(parsed, mode, fromSheet) {

      const rows = parsed.rows;

      const known = new Map();
      const byText = new Map();

      Object.values(checklist).forEach(section => {

        section.criteria.forEach(criterion => {

          known.set(criterion.id, criterion);
          byText.set(criterion.text.trim().toLowerCase(), criterion);

        });

      });

      const snapshot = getPageSnapshot();
      const beforeById = new Map(snapshot.items.map(item => [item.id, item]));

      const updates = new Map();
      const warnings = [];

      rows.forEach((row, index) => {

        if (!row || typeof row !== "object") {
          return;
        }

        /*
         * Spreadsheet rows start at line 2 (line 1 is the header).
         */

        const line = fromSheet ? `Row ${index + 2}` : `Item ${index + 1}`;

        const rawId = pickField(row, ["id"]);
        const rawText = pickField(row, ["criterion", "text"]);

        let criterion = null;

        if (rawId !== undefined && String(rawId).trim() !== "") {
          criterion = known.get(String(rawId).trim()) || null;
        }

        if (!criterion && rawText !== undefined && String(rawText).trim() !== "") {
          criterion = byText.get(String(rawText).trim().toLowerCase()) || null;
        }

        if (!criterion) {

          const allEmpty = Object.values(row).every(value => String(value).trim() === "");

          if (!allEmpty) {
            warnings.push(`${line}: unknown criterion "${rawId || rawText || "?"}", skipped.`);
          }

          return;

        }

        const values = {};

        const rawSelected = pickField(row, ["selected", "check", "checked"]);

        if (rawSelected !== undefined) {

          const selected = parseSelected(rawSelected);

          if (selected === null) {
            warnings.push(`${line} (${criterion.id}): invalid Selected value "${rawSelected}", kept current value.`);
          } else {
            values.selected = selected;
          }

        }

        const rawPriority = pickField(row, ["priority"]);

        if (rawPriority !== undefined) {

          const priority = parsePriority(rawPriority);

          if (priority === null) {
            warnings.push(`${line} (${criterion.id}): invalid Priority "${rawPriority}" (use M, S or O), kept current value.`);
          } else {
            values.priority = priority;
          }

        }

        const rawStatus = pickField(row, ["status"]);

        if (rawStatus !== undefined) {

          const status = parseStatus(rawStatus);

          if (status === null) {
            warnings.push(`${line} (${criterion.id}): invalid Status "${rawStatus}" (use D, TD or R), kept current value.`);
          } else {
            values.status = status;
          }

        }

        const rawNotes = pickField(row, ["notes", "note", "comments", "comment"]);

        if (rawNotes !== undefined) {
          values.notes = rawNotes === null ? "" : String(rawNotes);
        }

        if (updates.has(criterion.id)) {
          warnings.push(`${line}: "${criterion.id}" appears more than once; the last row was used.`);
        }

        updates.set(criterion.id, values);

      });

      if (updates.size === 0) {
        throw new Error("No checklist criteria were found in the file. Make sure it has an ID column (as in an exported file).");
      }

      /*
       * Remember the state so the import can be undone.
       */

      lastImportSnapshot = snapshot;

      if (mode === "replace") {

        known.forEach((criterion, id) => {

          if (!updates.has(id)) {
            setCriterionValues(id, { selected: false, priority: "", status: "", notes: "" });
          }

        });

      }

      updates.forEach((values, id) => setCriterionValues(id, values));

      /*
       * Category order.
       */

      let orderChanged = false;

      if (parsed.sectionOrder) {

        const unknownSections = parsed.sectionOrder.filter(name => !checklist[name]);

        unknownSections.forEach(name => {
          warnings.push(`Unknown category "${name}" in the category order, ignored.`);
        });

        applySectionOrder(parsed.sectionOrder);

        orderChanged = getSectionOrder().join("\n") !== snapshot.order.join("\n");

      }

      /*
       * Notes column: follow the file setting (JSON), otherwise show
       * the column when the file contains notes.
       */

      const afterItems = getChecklistState();

      if (parsed.showNotes !== undefined) {
        setNotesVisible(parsed.showNotes);
      } else if (afterItems.some(item => item.notes.trim() !== "")) {
        setNotesVisible(true);
      }

      /*
       * Count and highlight what changed.
       */

      let changed = 0;

      afterItems.forEach(item => {

        const previous = beforeById.get(item.id);

        const differs =
          previous.selected !== item.selected ||
          previous.priority !== item.priority ||
          previous.status !== item.status ||
          previous.notes !== item.notes;

        if (differs) {

          changed++;

          const checkbox = document.getElementById(item.id);
          const row = checkbox ? checkbox.closest("tr") : null;

          if (row) {
            row.classList.remove("imported-change");
            void row.offsetWidth;
            row.classList.add("imported-change");
          }

        }

      });

      return {
        matched: updates.size,
        total: known.size,
        changed: changed,
        orderChanged: orderChanged,
        warnings: warnings
      };

    }


    function escapeHtml(text) {

      const div = document.createElement("div");

      div.textContent = text;

      return div.innerHTML;

    }


    function showImportReport(type, message, warnings) {

      const report = document.getElementById("import-report");

      if (!report) {
        return;
      }

      let html = `<p><strong>${type === "error" ? "Import failed:" : "Done:"}</strong> ${escapeHtml(message)}</p>`;

      if (warnings && warnings.length > 0) {

        html += `<details open><summary>${warnings.length} warning${warnings.length === 1 ? "" : "s"}</summary><ul>`;

        warnings.forEach(warning => {
          html += `<li>${escapeHtml(warning)}</li>`;
        });

        html += "</ul></details>";

      }

      report.className = `import-report ${type}`;
      report.innerHTML = html;

    }


    async function handleImport(event) {

      event.preventDefault();

      const form = event.target;
      const input = document.getElementById("import-file");
      const file = input.files && input.files[0];

      if (!file) {
        showImportReport("error", "Choose a file to import.");
        return;
      }

      const mode = form.elements["import_mode"].value || "merge";

      try {

        const content = await readFile(file);

        const fromSheet = typeof content !== "string";

        let parsed;

        if (fromSheet) {

          parsed = parseWorkbookImport(content);

        } else {

          let data;

          try {
            data = JSON.parse(content);
          } catch (error) {
            throw new Error("The file is not valid JSON.");
          }

          parsed = parseJsonImport(data);

        }

        const result = applyImport(parsed, mode, fromSheet);

        let message =
          `"${file.name}" imported. ${result.matched} of ${result.total} criteria found in the file, ${result.changed} changed on the page.`;

        if (result.orderChanged) {
          message += " The category order was updated.";
        }

        showImportReport(
          result.warnings.length > 0 ? "warning" : "success",
          message,
          result.warnings
        );

        document.getElementById("import-undo").hidden = false;

        input.value = "";

      } catch (error) {

        console.error(error);

        showImportReport("error", error.message || String(error));

      }

    }


    function undoImport() {

      if (!lastImportSnapshot) {
        return;
      }

      lastImportSnapshot.items.forEach(item => setCriterionValues(item.id, item));

      applySectionOrder(lastImportSnapshot.order);

      setNotesVisible(lastImportSnapshot.showNotes);

      lastImportSnapshot = null;

      document.getElementById("import-undo").hidden = true;

      showImportReport("success", "The last import was undone.");

    }


    function setupControls() {

      const notesToggle = document.getElementById("toggle-notes");
      const resetOrderButton = document.getElementById("reset-order");
      const exportXlsxButton = document.getElementById("export-xlsx");
      const exportJsonButton = document.getElementById("export-json");
      const importForm = document.getElementById("import-form");
      const undoButton = document.getElementById("import-undo");

      if (notesToggle) {

        notesToggle.checked = areNotesVisible();

        notesToggle.addEventListener("change", () => setNotesVisible(notesToggle.checked));

      }

      if (resetOrderButton) {
        resetOrderButton.addEventListener("click", () => applySectionOrder(Object.keys(checklist)));
      }

      if (exportXlsxButton) {
        exportXlsxButton.addEventListener("click", exportXlsx);
      }

      if (exportJsonButton) {
        exportJsonButton.addEventListener("click", exportJson);
      }

      if (importForm) {
        importForm.addEventListener("submit", handleImport);
      }

      if (undoButton) {
        undoButton.addEventListener("click", undoImport);
      }

      updateSectionControls();

    }


    /*
     * Render the checklist when the page loads.
     */

    document.addEventListener(
      "DOMContentLoaded",
      () => {
        renderChecklist();
        setupControls();
      }
    );

  </script>

</body>