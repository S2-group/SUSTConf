---
layout: page
title: SUSTConf Framework
subtitle: A Framework for Sustainability-Aware Conferences
permalink: /framework/
---

<script src="../assets/data/sustConf-checklist-data.js"></script>

  <style>

    body {
      font-family: Lora, Arial, sans-serif;
      line-height: 1.5;
      margin: 2rem;
      color: #222;
    }


    h1 {
      margin-bottom: 0.25rem;
    }


    h2 {
      margin-top: 2rem;
    }


    h3 {
      margin-top: 1.5rem;
    }


    table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 2rem;
    }


    th,
    td {
      border: 1px solid #ccc;
      padding: 0.6rem;
      text-align: left;
      vertical-align: top;
    }


    th {
      background: #f5f5f5;
    }


    /* =========================================================
       Checkbox column
       ========================================================= */

    th.check-column,
    td.check-column {
      width: 50px;
      text-align: center;
      vertical-align: middle;
    }


    /* =========================================================
       Criterion column
       ========================================================= */

    th.criterion-column {
      width: auto;
    }


    /* =========================================================
       Priority and status columns
       ========================================================= */

    th.priority-column,
    th.status-column {
      width: 20%;
    }


    /* =========================================================
       Resources column
       ========================================================= */

    th.resources-column,
    td.resources-column {
      width: 100px;
      text-align: center;
      vertical-align: middle;
    }


    td.resources-column a {
      text-decoration: none;
      font-weight: bold;
    }


    td.resources-column a:hover {
      text-decoration: underline;
    }


    td.check-column input[type="checkbox"] {
      width: 18px;
      height: 18px;
      cursor: pointer;
    }


    label {
      cursor: pointer;
    }


    select {
      padding: 0.35rem;
      width: 100%;
      max-width: 220px;
    }


    section {
      margin-bottom: 2rem;
    }


    .intro {
      margin-bottom: 2rem;
    }

    /* =========================================================
       Framework overview and pipeline
       ========================================================= */

    .framework-intro {
      max-width: 900px;
    }

    .framework-intro .lead {
      font-size: 1.2rem;
      line-height: 1.6;
    }

    .framework-pipeline {
      margin: 3rem 0 3.5rem;
    }

    .pipeline-header {
      max-width: 900px;
      margin-bottom: 2rem;
    }

    .pipeline-kicker {
      display: block;
      margin-bottom: 0.4rem;
      font-size: 0.78rem;
      font-weight: bold;
      letter-spacing: 0.12em;
      color: #666;
    }

    .pipeline-header h2 {
      margin: 0 0 0.5rem;
    }

    .pipeline-header p {
      margin: 0;
      color: #555;
      max-width: 800px;
    }

    .pipeline {
      display: flex;
      flex-direction: column;
      gap: 0;
      position: relative;
      max-width: 1000px;
    }

    .pipeline-step {
      position: relative;
      display: grid;
      grid-template-columns: 3.5rem 1fr;
      gap: 1.25rem;
      border: 1px solid #d8d8d8;
      background: #fff;
      padding: 1.4rem 1.5rem;
      min-height: 0;
    }

    .pipeline-step + .pipeline-step {
      border-top: none;
    }

    .pipeline-step:not(:last-child)::after {
      content: "↓";
      position: absolute;
      left: 1.05rem;
      bottom: -0.8rem;
      z-index: 2;
      width: 1.5rem;
      height: 1.5rem;
      text-align: center;
      line-height: 1.35rem;
      background: #fff;
      color: #777;
      font-size: 1.2rem;
      font-weight: bold;
    }

    .start-step {
      border: 2px solid #555;
    }

    .step-number {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 2.5rem;
      height: 2.5rem;
      border: 1px solid #777;
      border-radius: 50%;
      font-weight: bold;
    }

    .step-phase {
      display: block;
      margin-bottom: 0.45rem;
      font-size: 0.72rem;
      line-height: 1.3;
      font-weight: bold;
      letter-spacing: 0.06em;
      color: #666;
    }

    .step-content {
      max-width: 850px;
    }

    .step-content h3 {
      margin: 0 0 0.7rem;
    }

    .step-content p {
      margin: 0;
      color: #444;
    }

    .step-callout {
      margin-top: 1.2rem;
      padding: 0.8rem;
      border-left: 3px solid #555;
      background: #f5f5f5;
      font-size: 0.92rem;
    }

    .pipeline-footer {
      margin-top: 1.5rem;
      padding: 1.1rem 1.3rem;
      border-top: 2px solid #222;
      border-bottom: 1px solid #ccc;
    }

    .pipeline-footer strong {
      font-size: 1.05rem;
    }

    .pipeline-footer p {
      margin: 0.35rem 0 0;
      color: #555;
    }

    @media (max-width: 600px) {
      .pipeline-step {
        grid-template-columns: 2.8rem 1fr;
        gap: 0.9rem;
        padding: 1.2rem;
      }

      .pipeline-step:not(:last-child)::after {
        left: 0.7rem;
      }
    }


    .legend {
      background: #f8f8f8;
      border: 1px solid #ddd;
      padding: 1rem 1.5rem;
      margin: 1.5rem 0;
    }


    .legend p {
      margin-top: 0.25rem;
    }


    .instructions {
      background: #f8f8f8;
      border-left: 4px solid #999;
      padding: 1rem 1.5rem;
      margin: 1.5rem 0 2rem;
    }


    .sources {
      margin-top: 4rem;
      padding-top: 2rem;
      border-top: 2px solid #ccc;
    }


    .sources li {
      margin-bottom: 0.5rem;
    }


    .methodology {
      margin-bottom: 2rem;
    }


    .error {
      padding: 1rem;
      background: #ffe6e6;
      border: 1px solid #cc0000;
      color: #990000;
    }

  </style>



<body>

  <main>

<header class="intro framework-intro">

  <p class="lead">
    The <strong>SUSTConf Framework</strong> is a collection of reusable resources
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
      Start with the checklist, use the framework resources to prepare the selected
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
          Sustainability Chairs use the reusable resources provided by the framework
          to design and set up the actions selected in the checklist. The resources
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
      <strong>Checklist → Resources → Actions → Metrics → Report</strong>
    </div>
    <p>
      The checklist establishes what the conference intends to do; the framework
      resources support how it is done; the pipeline ensures that actions are
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

</section>


<!-- =========================================================
     CHECKLIST
     ========================================================= -->

<div id="checklist"></div>


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
       RESOURCE COUNTS
       =========================================================

       Resource posts are Jekyll posts tagged "resource".

       Every additional tag on a resource post is treated as
       a resource category.

       The category/tag is the same as the checklist criterion ID.

       Example:

         tags:
           - resource
           - food_local

       The checklist criterion:

         id: food_local

       will therefore show the number of matching resource posts.
       ========================================================= -->

  <script>

    /*
     * Resource counts.
     *
     * Liquid collects all tags used by resource posts and counts
     * how many resource posts use each tag.
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


          /*
           * Section heading.
           */

          const heading =
            document.createElement("h2");


          heading.textContent =
            sectionName;


          sectionElement.appendChild(
            heading
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
           * Resources column.
           */

          const resourcesHeader =
            document.createElement("th");


          resourcesHeader.textContent =
            "Resources";


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
               * Resources
               * --------------------------------------------------
               */

              const resourcesCell =
                document.createElement("td");


              resourcesCell.className =
                "resources-column";


              const resourceCount =
                resourceCounts[criterion.id] || 0;


              /*
               * If resources exist, make the number a link.
               *
               * Example:
               *
               *   /resources/?type=food_local
               *
               * The Resources page can then use the "type"
               * parameter to filter the resources.
               */

              if (resourceCount > 0) {

                const resourcesLink =
                  document.createElement("a");


                resourcesLink.href =
                  `{{ '/resources/' | relative_url }}?type=${encodeURIComponent(criterion.id)}`;


                resourcesLink.textContent =
                  resourceCount;


                resourcesLink.className =
                  "resources-count-link";


                resourcesLink.setAttribute(
                  "aria-label",
                  `View ${resourceCount} resources for ${criterion.text}`
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
     * Render the checklist when the page loads.
     */

    document.addEventListener(
      "DOMContentLoaded",
      () => {
        renderChecklist();
      }
    );

  </script>

</body>