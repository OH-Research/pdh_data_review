---
layout: post
provider: "Ministry of Health"
id: "new_zealand_health_survey_child_health_status_and_behaviours_2014_15"
title: "New Zealand Health Survey: Child health status and behaviours 2014/15"
link: "https://www.health.govt.nz/publication/annual-update-key-results-2014-15-new-zealand-health-survey"
categories: new-zealand government 
tags:
  - childhood
  - global-health
  - figure.nz
figure_nz:
  - item:
    title_l1: New Zealand children with excellent, very good or good health, as rated by their parent
    title_l2_list:
      - by sex and ethnic group|https://figure.nz/chart/qcV50t6S4Kj4mHJF-IQoUcXzefbNxIJVa
      - by sex and neighbourhood deprivation|https://figure.nz/chart/qcV50t6S4Kj4mHJF-L5QrwO7reoTYHz7Q
      - by sex and age group|https://figure.nz/chart/qcV50t6S4Kj4mHJF-hDeI1tMxVwArxbri           
---

This dataset provides a snapshot of the health of New Zealanders through the publication of key indicators on health behaviours, health status and access to health care. See the table "Child data tables: Health status, health behaviours and risk factors".

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