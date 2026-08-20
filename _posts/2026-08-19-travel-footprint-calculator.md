---
layout: post
title: Carbon Footprint Calculator
subtitle: An open-source carbon footprint calculator to calculate the impact of your conference
#gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: 
  - resource 
  - transport_carbon_calculator 
comments: true
mathjax: true
author: Andrea Janes (Free University Bozen/Bolzano)
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

  </section>

  <!-- How it works -->
  <section class="mb-5">
    <h2>How it works?</h2>

    <p>
      The tool is designed around the reality of conference travel. A
      participant may use several modes of transportation before reaching the
      conference destination, so the tool supports journeys with multiple
      legs.
    </p>

   <div class="mt-4">

  <div class="d-flex gap-3 mb-4">
    <div class="process-number flex-shrink-0">1</div>
    <div>
      <h3>Enter the journey</h3>
      <p>
        Participants enter their starting location and the different legs
        of their journey.
      </p>
      <p class="mb-0">
        For example:
        <strong>home → train station → airport → conference city</strong>.
      </p>
    </div>
  </div>

  <div class="d-flex gap-3 mb-4">
    <div class="process-number flex-shrink-0">2</div>
    <div>
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

  <div class="d-flex gap-3">
    <div class="process-number flex-shrink-0">3</div>
    <div>
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



  <!-- How conferences can use it -->
  <section class="mb-5">
    <h2>How conferences can use the tool?</h2>

    <p>
      The calculator can be integrated into the registration process or
      presented as an optional travel-planning tool. The resulting information
      can then support both immediate communication and longer-term
      sustainability planning.
    </p>
<div class="conference-use-cases mt-4">

  <div class="d-flex gap-3 mb-4">
    <div>
      <h3>During registration</h3>
      <p>
        Invite participants to describe their expected journey when they register for the conference. This makes sustainable travel part of the conversation from the beginning.
      </p>
    </div>
  </div>

  <div class="d-flex gap-3 mb-4">
    <div>
      <h3>After the conference</h3>
      <p>
        Aggregate the collected information to understand the overall travel profile of your event. Use the results to identify the biggest sources of emissions.
      </p>
    </div>
  </div>

  <div class="d-flex gap-3">
    <div>
      <h3>For future conferences</h3>
      <p>
        Compare results across editions and use the evidence to guide future decisions about locations, travel and conference design. Measurement makes improvement possible.
      </p>
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