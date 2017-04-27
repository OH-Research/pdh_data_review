---
layout: post
provider: "Ministry of Health"
id: "new_zealand_health_survey_adult_health_service_use_unmet_need_and_oral_health_2014_15"
title: "New Zealand Health Survey: Adult health service use, unmet need and oral health 2014/15"
link: "https://www.health.govt.nz/publication/annual-update-key-results-2014-15-new-zealand-health-survey"
categories: new-zealand government 
tags:
  - global-health
  - figure.nz
figure_nz:
  - item:
    title_l1: New Zealand adults who experienced one or more types of unmet need for primary health care in the past 12 months
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/ezLphNZ2CqUWQvP0-lsUYbuUkO1DlE7df
      - by sex and age group|https://figure.nz/chart/ezLphNZ2CqUWQvP0-61KR1Xke6cDnj1WH
      - by sex and neighbourhood deprivation|https://figure.nz/chart/ezLphNZ2CqUWQvP0-OEFpOlK2aA4whQ6Z
  - item:
    title_l1: New Zealand adults who never visit a dental health care worker, or only visit when they have dental problems
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/RSc5JSypFbotVAeu-6LJwTuLrhZlX1lfZ
      - by sex and age group|https://figure.nz/chart/RSc5JSypFbotVAeu-VASw52biLycLoSil
      - by sex and neighbourhood deprivation|https://figure.nz/chart/RSc5JSypFbotVAeu-vCQBtisUEjEJzUEt
  - item:
    title_l1: New Zealand adults who thought their GP was very good or good at explaining health conditions and treatments
    title_l2_list:
      - by sex and ethnicity|https://figure.nz/chart/Z5KLd9StSo4p0rrw-OlH4V9L6j6yz0BHc
      - by sex and neighbourhood deprivation|https://figure.nz/chart/Z5KLd9StSo4p0rrw-CtweRTrFnNWv271M
      - by sex and age group|https://figure.nz/chart/Z5KLd9StSo4p0rrw-pjRchTn74lsKOaKj
  - item:
    title_l1: New Zealand adults who visited a dental health care worker in the past 12 months
    title_l2_list:
      - by sex and neighbourhood deprivation|https://figure.nz/chart/oVTvRD1fWXY20EUp-on3RVfnhmX9b4r5r
      - by sex and ethnicity|https://figure.nz/chart/oVTvRD1fWXY20EUp-kXvFhvUVlfplJCb5
      - by sex and age group|https://figure.nz/chart/oVTvRD1fWXY20EUp-CuFfYBKRFZpL8all
---

This dataset provides a snapshot of the health of New Zealanders through the publication of key indicators on health behaviours, health status and access to health care. See the "Adult data tables: Health service use, unmet need and oral health".

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