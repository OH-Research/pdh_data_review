---
layout: post
provider: "Ministry of Health"
id: "new_zealand_health_survey_adult_health_status_behaviours_and_risk_factors_2014_15"
title: "New Zealand Health Survey: Adult health status - behaviours and risk factors 2014/15"
link: "https://www.health.govt.nz/publication/annual-update-key-results-2014-15-new-zealand-health-survey"
categories: new-zealand government 
tags:
  - global-health
  - figure.nz
figure_nz:
  - item:
    title_l1: New Zealand adults who rated their health as good, very good or excellent
    title_l2_list:
      - by sex and neighbourhood deprivation|https://figure.nz/chart/du1Y79ZPFZdxDR7D-vmok9PxqSllQQjNm
      - by sex and ethnicity|https://figure.nz/chart/du1Y79ZPFZdxDR7D-XfcW8XEhQ024cvyS
      - by sex and age group|https://figure.nz/chart/du1Y79ZPFZdxDR7D-FtMP42mhydmaBjyi      
---

This dataset provides a snapshot of the health of New Zealanders through the publication of key indicators on health behaviours, health status and access to health care. See the table "Adult data tables: Health status, health behaviours and risk factors".

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