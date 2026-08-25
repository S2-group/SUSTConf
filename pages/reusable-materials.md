---
layout: page
title: Reusable Materials
subtitle: Reusable materials for your conference
permalink: /reusable-materials/
wide-content: true
---
{% assign resource_posts = site.posts | where_exp: "post", "post.tags contains 'resource'" %}

{% comment %}
Collect all tags used by reusable materials, excluding the "resource" tag itself.
{% endcomment %}

{% assign resource_types = "" | split: "" %}

{% for post in resource_posts %}
{% for tag in post.tags %}
{% unless tag == "resource" %}
{% unless resource_types contains tag %}
{% assign resource_types = resource_types | push: tag %}
{% endunless %}
{% endunless %}
{% endfor %}
{% endfor %}

<div class="resources">

  <!-- Reusable material filters -->

  <div class="resources-filter">

<div class="resources-filter-header">
  <div>
    <h2 class="resources-filter-title">Available Reusable Materials</h2>
    <p class="resources-filter-description">
      Browse reusable materials for your conference and filter them by type.
    </p>
  </div>

  <div class="resources-count">
    <span id="resources-visible-count">{{ resource_posts.size }}</span>
    <span>reusable materials</span>
  </div>
</div>

<div class="resources-filter-controls">

  <div class="resources-filter-group">
    <label for="resource-type-filter" class="resources-filter-label">
      Reusable material type
    </label>

    <select
      id="resource-type-filter"
      class="form-select resources-filter-select"
      aria-label="Filter reusable materials by type">

      <option value="all">All reusable materials</option>

      {% assign sorted_resource_types = resource_types | sort %}
      {% for type in sorted_resource_types %}
        <option value="{{ type | slugify }}">
          {{ type | replace: '-', ' ' | capitalize }}
        </option>
      {% endfor %}

    </select>
  </div>

  <div class="resources-search-group">
    <label for="resource-search" class="resources-filter-label">
      Search
    </label>

    <input
      type="search"
      id="resource-search"
      class="form-control resources-search-input"
      placeholder="Search reusable materials..."
      aria-label="Search reusable materials">
  </div>

</div>

  </div>

  <!-- Reusable materials table -->

  <div class="resources-table-wrapper">

{% if resource_posts.size > 0 %}

  <table class="resources-table">
    <thead>
      <tr>
        <th scope="col" class="resource-name-column">
          Reusable Material
        </th>

        <th scope="col" class="resource-type-column">
          Type
        </th>

        <th scope="col" class="resource-author-column">
          Author
        </th>

        <th scope="col" class="resource-link-column">
          Links
        </th>

      </tr>
    </thead>

    <tbody id="resources-table-body">

      {% assign sorted_resources = resource_posts | sort: "title" %}

      {% for post in sorted_resources %}

        {% assign resource_tags = "" | split: "" %}

        {% for tag in post.tags %}
          {% unless tag == "resource" %}
            {% assign resource_tags = resource_tags | push: tag %}
          {% endunless %}
        {% endfor %}

        <tr
          class="resource-row"
          data-resource-tags="{% for tag in resource_tags %}{{ tag | slugify }}{% unless forloop.last %} {% endunless %}{% endfor %}"
          data-resource-search="{{ post.title | downcase }} {{ post.subtitle | default: '' | downcase }} {% for tag in resource_tags %}{{ tag | downcase }} {% endfor %} {{ post.author | default: '' | downcase }}">

          <td class="resource-name-cell">

            <div class="resource-name-wrapper">

              <a
                href="{{ post.url | relative_url }}"
                class="resource-title">
                {{ post.title | strip_html }}
              </a>

              {% if post.subtitle %}
                <p class="resource-description">
                  {{ post.subtitle | strip_html }}
                </p>
              {% endif %}

            </div>

          </td>


          <td class="resource-type-cell">

            <div class="resource-tags">

              {% for tag in resource_tags %}

                <span
                  class="resource-tag"
                  data-tag="{{ tag | slugify }}">
                  {{ tag | replace: '-', ' ' | capitalize }}
                </span>

              {% endfor %}

            </div>

          </td>


          <td class="resource-author-cell">

            {% if post.author %}
              {{ post.author | strip_html }}
            {% else %}
              <span class="resource-no-value">—</span>
            {% endif %}

          </td>


          <td class="resource-link-cell">
            <a
              href="{{ post.url | relative_url }}"
              class="resource-link"
              aria-label="Open {{ post.title | strip_html }}">
              Link
            </a>
          </td>


        </tr>

      {% endfor %}

    </tbody>
  </table>


  <!-- Empty search/filter state -->
  <div
    id="resources-empty-state"
    class="resources-empty-state"
    hidden>

    <div class="resources-empty-icon" aria-hidden="true">
      🔎
    </div>

    <h3>No reusable materials found</h3>

    <p>
      Try selecting another reusable material type or changing your search.
    </p>

    <button
      type="button"
      id="resources-reset-button"
      class="btn btn-outline-success">

      Reset filters

    </button>

  </div>

{% else %}

  <div class="resources-empty-state resources-empty-state-static">

    <div class="resources-empty-icon" aria-hidden="true">
      📚
    </div>

    <h3>No reusable materials available yet</h3>

    <p>
      Reusable conference materials will appear here as they are added.
    </p>

  </div>

{% endif %}

  </div>

</div>

<style>

  @media (min-width: 992px) {

    .wide-content-page > .row > .wide-content-column {
      flex: 0 0 91.666667%;
      max-width: 91.666667%;
      margin-left: 4.166667%;
    }

  }

  @media (min-width: 1200px) {

    .wide-content-page > .row > .wide-content-column {
      flex: 0 0 83.333333%;
      max-width: 83.333333%;
      margin-left: 8.333333%;
    }

  }

  /* ============================================================
     Resources page
     ============================================================ */

  .resources {
    margin-top: 2rem;
  }


  /* ============================================================
     Filter area
     ============================================================ */

  .resources-filter {
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: #F7FAF5;
    border: 1px solid #C9D9CD;
    border-radius: 1rem;
  }

  .resources-filter-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
  }

  .resources-filter-title {
    margin: 0 0 0.35rem;
    color: #2F3A32;
    font-size: 1.5rem;
    font-weight: 600;
  }

  .resources-filter-description {
    margin: 0;
    color: #5F6F63;
  }

  .resources-count {
    flex-shrink: 0;
    padding: 0.45rem 0.75rem;
    border-radius: 999px;
    background: #E4EEE7;
    color: #2E7D5B;
    font-size: 0.9rem;
    font-weight: 600;
    white-space: nowrap;
  }

  .resources-filter-controls {
    display: grid;
    grid-template-columns: minmax(200px, 280px) minmax(250px, 1fr);
    gap: 1rem;
  }

  .resources-filter-group,
  .resources-search-group {
    min-width: 0;
  }

  .resources-filter-label {
    display: block;
    margin-bottom: 0.45rem;
    color: #2F3A32;
    font-size: 0.9rem;
    font-weight: 600;
  }

  .resources-filter-select,
  .resources-search-input {
    min-height: 44px;
    border: 1px solid #C9D9CD;
    border-radius: 0.6rem;
    color: #2F3A32;
    background-color: #fff;
  }

  .resources-filter-select:focus,
  .resources-search-input:focus {
    border-color: #2E7D5B;
    box-shadow: 0 0 0 0.2rem rgba(46, 125, 91, 0.15);
  }


  /* ============================================================
     Table
     ============================================================ */

  .resources-table-wrapper {
    width: 100%;
    overflow-x: auto;
    border: 1px solid #E1E8E2;
    border-radius: 1rem;
    background: #fff;
  }

  .resources-table {
    width: 100%;
    margin: 0;
    border-collapse: separate;
    border-spacing: 0;
  }

  .resources-table thead {
    background: #F7FAF5;
  }

  .resources-table th {
    padding: 1rem 1.25rem;
    border-bottom: 1px solid #DCE5DE;
    color: #5F6F63;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-align: left;
    text-transform: uppercase;
    white-space: nowrap;
  }

  .resources-table td {
    padding: 1.15rem 1.25rem;
    border-bottom: 1px solid #E8EEE9;
    vertical-align: middle;
  }

  .resources-table tbody tr:last-child td {
    border-bottom: 0;
  }

  .resources-table tbody tr {
    transition:
      background-color 0.15s ease,
      box-shadow 0.15s ease;
  }

  .resources-table tbody tr:hover {
    background-color: #FAFCFA;
  }


  /* ============================================================
     Columns
     ============================================================ */

  .resource-name-column {
    width: 55%;
  }

  .resource-type-column {
    width: 25%;
  }

  .resource-author-column {
    width: 20%;
  }

  .resource-link-column {
    width: 15%;
  }



  /* ============================================================
     Resource content
     ============================================================ */

  .resource-name-wrapper {
    min-width: 240px;
  }

  .resource-title {
    display: inline-block;
    color: #2F3A32;
    font-size: 1.05rem;
    font-weight: 600;
    line-height: 1.4;
    text-decoration: none;
  }

  .resource-title:hover,
  .resource-title:focus {
    color: #2E7D5B;
    text-decoration: underline;
  }

  .resource-description {
    max-width: 650px;
    margin: 0.4rem 0 0;
    color: #6B776E;
    font-size: 0.9rem;
    line-height: 1.5;
  }


  /* ============================================================
     Tags
     ============================================================ */

  .resource-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }

  .resource-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.3rem 0.6rem;
    border: 1px solid #C9D9CD;
    border-radius: 999px;
    background: #F7FAF5;
    color: #2E7D5B;
    font-size: 0.78rem;
    font-weight: 600;
    line-height: 1.2;
    white-space: nowrap;
  }


  /* ============================================================
     Author
     ============================================================ */

  .resource-author-cell {
    color: #5F6F63;
    font-size: 0.9rem;
  }

  .resource-link {
    color: #2E7D5B;
    font-weight: 600;
    text-decoration: underline;
  }

  .resource-link:hover,
  .resource-link:focus {
    color: #225D44;
  }

  .resource-no-value {
    color: #A0AAA3;
  }



  /* ============================================================
     Empty state
     ============================================================ */

  .resources-empty-state {
    padding: 4rem 2rem;
    text-align: center;
  }

  .resources-empty-icon {
    margin-bottom: 1rem;
    font-size: 2.5rem;
  }

  .resources-empty-state h3 {
    margin-bottom: 0.5rem;
    color: #2F3A32;
    font-weight: 600;
  }

  .resources-empty-state p {
    margin-bottom: 1.5rem;
    color: #6B776E;
  }


  /* ============================================================
     Responsive layout
     ============================================================ */

  @media (max-width: 767.98px) {

    .resources-filter {
      padding: 1.25rem;
    }

    .resources-filter-header {
      display: block;
    }

    .resources-count {
      display: inline-block;
      margin-top: 1rem;
    }

    .resources-filter-controls {
      grid-template-columns: 1fr;
    }

    .resources-table-wrapper {
      border: 0;
      overflow: visible;
      background: transparent;
    }

    .resources-table,
    .resources-table thead,
    .resources-table tbody,
    .resources-table tr,
    .resources-table th,
    .resources-table td {
      display: block;
    }

    .resources-table thead {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }

    .resources-table tbody {
      display: grid;
      gap: 1rem;
    }

    .resources-table tbody tr {
      padding: 1.25rem;
      border: 1px solid #E1E8E2;
      border-radius: 0.9rem;
      background: #fff;
    }

    .resources-table tbody tr:hover {
      background-color: #fff;
    }

    .resources-table td {
      width: 100% !important;
      padding: 0;
      border: 0;
    }

    .resources-table td + td {
      margin-top: 0.9rem;
      padding-top: 0.9rem;
      border-top: 1px solid #E8EEE9;
    }

    .resource-name-wrapper {
      min-width: 0;
    }

    .resource-description {
      max-width: none;
    }

    .resource-type-cell::before,
    .resource-author-cell::before,
    .resource-link-cell::before {
      display: block;
      margin-bottom: 0.35rem;
      color: #7A857D;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .resource-type-cell::before {
      content: "Type";
    }

    .resource-author-cell::before {
      content: "Author";
    }

    .resource-link-cell::before {
      content: "Links";
    }


  }


  @media (max-width: 575.98px) {

    .resources-filter-title {
      font-size: 1.3rem;
    }

    .resources-filter-description {
      font-size: 0.9rem;
    }

    .resource-title {
      font-size: 1rem;
    }

    .resource-description {
      font-size: 0.85rem;
    }

  }

</style>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    const typeFilter = document.getElementById('resource-type-filter');
    const searchInput = document.getElementById('resource-search');
    const tableBody = document.getElementById('resources-table-body');
    const emptyState = document.getElementById('resources-empty-state');
    const resetButton = document.getElementById('resources-reset-button');
    const visibleCount = document.getElementById('resources-visible-count');

    if (!typeFilter || !searchInput || !tableBody) {
      return;
    }

    const rows = Array.from(
      tableBody.querySelectorAll('.resource-row')
    );

    /*
     * Normalize values before comparing them.
     *
     * The <option> values are generated by Liquid using `slugify`,
     * while the URL parameter may arrive as:
     *
     *   ?type=conference
     *   ?type=Conference
     *   ?type=conference-resources
     *
     * Normalizing both sides prevents case, spaces and URL-encoding
     * differences from breaking the filter.
     */
    function normalizeType(value) {
      if (!value) {
        return '';
      }

      return decodeURIComponent(String(value))
        .trim()
        .toLowerCase()
        .replace(/&/g, ' and ')
        .replace(/['"]/g, '')
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '');
    }

    function filterResources() {
      const selectedType = normalizeType(typeFilter.value);
      const searchTerm = searchInput.value
        .trim()
        .toLowerCase();

      let visibleResources = 0;

      rows.forEach(function (row) {
        const resourceTags = (row.dataset.resourceTags || '')
          .split(/\s+/)
          .filter(Boolean)
          .map(normalizeType);

        const searchableText = (
          row.dataset.resourceSearch || ''
        ).toLowerCase();

        const matchesType =
          selectedType === 'all' ||
          selectedType === '' ||
          resourceTags.includes(selectedType);

        const matchesSearch =
          searchTerm === '' ||
          searchableText.includes(searchTerm);

        const shouldShow = matchesType && matchesSearch;

        row.hidden = !shouldShow;

        if (shouldShow) {
          visibleResources++;
        }
      });

      if (visibleCount) {
        visibleCount.textContent = visibleResources;
      }

      if (emptyState) {
        emptyState.hidden = visibleResources !== 0;
      }
    }

    function resetFilters() {
      typeFilter.value = 'all';
      searchInput.value = '';

      filterResources();
      typeFilter.focus();
    }

    /*
     * Apply a type received through the URL.
     *
     * IMPORTANT:
     * Do this during DOMContentLoaded instead of waiting for `load`.
     * The original implementation initialized the filter in one
     * listener and applied the URL parameter in another listener.
     * That made the behaviour unnecessarily dependent on page-load
     * timing.
     */
    function applyUrlFilter() {
      const urlParams = new URLSearchParams(window.location.search);
      const typeParam = urlParams.get('type');

      if (!typeParam) {
        filterResources();
        return;
      }

      const normalizedParam = normalizeType(typeParam);

      /*
       * Find the actual <option> whose value corresponds to the
       * normalized URL parameter. This also handles parameters
       * supplied as human-readable tag names.
       */
      const matchingOption = Array.from(typeFilter.options).find(
        function (option) {
          return normalizeType(option.value) === normalizedParam;
        }
      );

      if (matchingOption) {
        typeFilter.value = matchingOption.value;
      } else {
        /*
         * If the URL contains an invalid/unknown type, fall back to
         * "all" instead of leaving the select in an inconsistent state.
         */
        typeFilter.value = 'all';
      }

      filterResources();
    }

    typeFilter.addEventListener('change', filterResources);
    searchInput.addEventListener('input', filterResources);

    if (resetButton) {
      resetButton.addEventListener('click', resetFilters);
    }

    applyUrlFilter();
  });
</script>

