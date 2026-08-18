---
layout: page
title: Resources
subtitle: Reusable resources for your conference
permalink: /resources/
---

<div class="resources">
  <div class="row g-4">
        <!-- Share a Resource -->
    <div class="col-12 col-md-6">
      <div class="card h-100 resource-contribute-card border-2">
        <div class="card-body p-4">
          <div class="resource-icon mb-3">🤝</div>

          <h3 class="card-title">Share a Resource</h3>

          <p class="card-text">
            Have a reusable resource that could help other conferences?
            Resource sharing is encouraged and welcome.
          </p>

          <p class="card-text">
            <strong>Want to contribute?</strong>
            Contact the framework maintainers to have your resource added here.
          </p>

          <div>p.lago at vu.nl</div>
          <div>vinicius.dos.santos at usp.br</div>
        </div>
      </div>
    </div>


    <!-- Sustainability Campaign -->
    <div class="col-12 col-md-6">
      <div class="card h-100 shadow-sm border-0">
        <div class="card-body p-4">
          <div class="resource-icon mb-3"><img src="../assets/img/train-green.jpg"></div>

          <h3 class="card-title">Sustainability Campaign</h3>

          <p class="card-text">
            Announce to everyone your commitment to sustainability and make
            your attendants more engaged to sustainability.
          </p>

          <a href="{{ '/sustainability-campaign/' | relative_url }}"
             class="btn btn-success">
            Explore the campaign
          </a>
        </div>
      </div>
    </div>

    <!-- Carbon Footprint Calculator -->
    <div class="col-12 col-md-6 mt-3">
    <div class="card h-100 shadow-sm border-0">
        <div class="card-body p-4">
        <div class="resource-icon mb-3">
            <img
            src="../assets/img/carbonFootprintCalculator.png"
            alt="Train travel as a sustainable transportation option"
            class="resource-image">
        </div>

        <h3 class="card-title">Carbon Footprint Calculator</h3>

        <p class="card-text">
            Help your conference understand the environmental impact of
            participant travel and collect data to support more sustainable
            decisions.
        </p>

        <a
            href="{{ '/carbon-footprint-calculator/' | relative_url }}"
            class="btn btn-success">
            Explore the calculator
        </a>
        </div>
    </div>
    </div>


  </div>
</div>

<style>
  .resources .card {
    border-radius: 1rem;
    transition:
      transform 0.2s ease,
      box-shadow 0.2s ease;
  }

  .resources .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 0.75rem 1.5rem rgba(47, 58, 50, 0.12) !important;
  }

  .resources .card-title {
    color: #2F3A32;
    font-weight: 600;
  }

  .resources .card-text {
    color: #5F6F63;
  }

  .resources .resource-icon {
    font-size: 2.25rem;
    line-height: 1;
  }

  .resources .btn-success {
    background-color: #2E7D5B;
    border-color: #2E7D5B;
  }

  .resources .btn-success:hover,
  .resources .btn-success:focus {
    background-color: #246B4C;
    border-color: #246B4C;
  }

  .resources .btn-outline-success {
    color: #2E7D5B;
    border-color: #2E7D5B;
  }

  .resources .btn-outline-success:hover,
  .resources .btn-outline-success:focus {
    background-color: #2E7D5B;
    border-color: #2E7D5B;
    color: #fff;
  }

  .resources .resource-contribute-card {
    background-color: #F7FAF5;
    border-color: #C9D9CD;
  }
</style>