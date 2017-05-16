---
layout: post
provider: "Ministry of Health"
id: "new_zealand_health_survey_child_health_conditions_2014_15"
title: "New Zealand Health Survey: Child health conditions 2014/15"
link: "https://www.health.govt.nz/publication/annual-update-key-results-2014-15-new-zealand-health-survey"
categories: new-zealand government 
tags:
  - childhood
  - global-health
  - figure.nz
figure_nz:
  - item:
    title_l1: New Zealand children diagnosed with asthma and currently taking medication
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/koF01s3mZnSpbsQK-iveitdlxaa4FH6Uk
      - by sex and neighbourhood deprivation|https://figure.nz/chart/koF01s3mZnSpbsQK-0iyE9eQBhKJeWqvO
      - by sex and age group|https://figure.nz/chart/EknP0H04o4QPpQzz
  - item:
    title_l1: New Zealand children diagnosed with eczema and currently taking medication
    title_l2_list:
      - by sex and neighbourhood deprivation|https://figure.nz/chart/4tJmF5Fv2yRf4rpy-8ktjFihrXliB2PWD
      - by sex and age group|https://figure.nz/chart/4tJmF5Fv2yRf4rpy-Qzx8d6cKHw5uca8r
      - by sex and ethnicity|https://figure.nz/chart/4tJmF5Fv2yRf4rpy-uZbwWC0tVkdXAL0H
  - item:
    title_l1: New Zealand children who were diagnosed with emotional or behavioural problems
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/Ao5wHsRYFO4zqftC-izrnZhH7xpvSqMqQ
      - by sex and neighbourhood deprivation|https://figure.nz/chart/Ao5wHsRYFO4zqftC-qjHKK2Aufy5MhSWe
      - by sex and age group|https://figure.nz/chart/NJK5lyicNRrnMACi           
---

This dataset provides a snapshot of the health of New Zealanders through the publication of key indicators on health behaviours, health status and access to health care. See the table "Child data tables: Health conditions".

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