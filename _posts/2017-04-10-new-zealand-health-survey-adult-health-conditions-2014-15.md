---
layout: post
provider: "Ministry of Health"
id: "new_zealand_health_survey_adult_health_conditions_2014_15"
title: "New Zealand Health Survey: Adult health conditions 2014/15"
link: "https://www.health.govt.nz/publication/annual-update-key-results-2014-15-new-zealand-health-survey"
categories: new-zealand government
tags:
  - global-health
  - figure.nz
figure_nz:
  - item:
    title_l1: New Zealand adults diagnosed with anxiety disorder
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/2HrfqSXVU6jCBDU9-Kift4dpRjApcQohd
      - by sex and neighbourhood deprivation|https://figure.nz/chart/2HrfqSXVU6jCBDU9-7KEXVBoiAkJs2fHz
      - by sex and age group|https://figure.nz/chart/2HrfqSXVU6jCBDU9-sAs9qKrEe47Ocsed
  - item:
    title_l1: New Zealand adults diagnosed with bipolar disorder
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/Bhb4Q3XlYaUwBV8J-TeQOdfnldt9krPwS
      - by sex and neighbourhood deprivation|https://figure.nz/chart/Bhb4Q3XlYaUwBV8J-Mq5XXjdlpHNqNunM
      - by sex and age group|https://figure.nz/chart/Bhb4Q3XlYaUwBV8J-aC1QXidJrOC3Xhd0
  - item:
    title_l1: New Zealand adults diagnosed with depression
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/ojfxVBkh2NaSUKCP-5ZL3H85O3bYFKrnv
      - by sex and neighbourhood deprivation|https://figure.nz/chart/ojfxVBkh2NaSUKCP-wuuhSJUTFc3Lkndy
      - by sex and age group|https://figure.nz/chart/ojfxVBkh2NaSUKCP-CMfmTHmZqHpqYXeD
  - item:
    title_l1: New Zealand adults diagnosed with mood disorders
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/XFMUaw3N3cP0bvqT-9uuF7UDVFXE1w6aT
      - by sex and neighbourhood deprivation|https://figure.nz/chart/XFMUaw3N3cP0bvqT-inUfJSa7XR1aMXM1
      - by sex and age group|https://figure.nz/chart/XFMUaw3N3cP0bvqT-DT9yTUlMVqCt0dHU
  - item:
    title_l1: New Zealand adults experiencing recent psychological distress
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/7wMXsesJ13yNUf8h-ymD9WwTxiTvQtM3i
      - by sex and neighbourhood deprivation|https://figure.nz/chart/7wMXsesJ13yNUf8h-Uza1yEFSnY3ZP2ns
      - by sex and age group|https://figure.nz/chart/7wMXsesJ13yNUf8h-8vJVZwMo6w5mAfJu
---

This dataset provides a snapshot of the health of New Zealanders through the publication of key indicators on health behaviours, health status and access to health care. See the table "Adult data tables: Health conditions".

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

