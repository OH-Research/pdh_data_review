---
layout: post
provider: "Ministry of Health"
id: "new_zealand_health_survey_hild_health_service_use_unmet_need_and_oral_health_2014_15"
title: "New Zealand Health Survey: Child health service use, unmet need and oral health 2014/15"
link: "https://www.health.govt.nz/publication/annual-update-key-results-2014-15-new-zealand-health-survey"
categories: new-zealand government 
tags:
  - childhood
  - global-health
  - figure.nz
figure_nz:
  - item:
    title_l1: New Zealand children who experienced one or more types of unmet need for primary health care in the past 12 months
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/Y8v7nltI8PEkpacK-AOqquy3Z3qMiCyBO
      - by sex and age group|https://figure.nz/chart/Y8v7nltI8PEkpacK-JbHxpytDvT87E7O4
      - by sex and neighbourhood deprivation|https://figure.nz/chart/Y8v7nltI8PEkpacK-vxnkSYQiDUjxtZ2C
  - item:
    title_l1: New Zealand children who visited a dental health care worker in the past 12 months
    title_l2_list:
      - by sex and neighbourhood deprivation|https://figure.nz/chart/2KqOpLfrTAJ0R6w1-Tzet59ISutlalfJD
      - by sex and ethnicity|https://figure.nz/chart/2KqOpLfrTAJ0R6w1-VSjAAABQiQpIItsd
      - by sex and age group|https://figure.nz/chart/oMlpoOTbIoBS5DAm         
---

This dataset provides a snapshot of the health of New Zealanders through the publication of key indicators on health behaviours, health status and access to health care. See the table "Child data tables: Health service use, unmet need and oral health".

<h4><u> More details on figure.nz</u></h4>
{% for item in page.figure_nz%}
  <ul class="post-list">
      <li>{{ item.title_l1 }}:</li>
  {% for l2 in item.title_l2_list %}
  	{% assign details = l2 | split: "|" %}
  	<ul class="post-list-l2">
      <li><a href="{{ details[1] }}">{{ details[0] }}</a></li>
  {% endfor %}
   </ul>
{% endfor %}
</ul>