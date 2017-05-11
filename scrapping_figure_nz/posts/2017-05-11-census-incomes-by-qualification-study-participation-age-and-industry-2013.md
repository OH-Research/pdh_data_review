---
categories: new-zealand survey
date: '2017-05-11 16:19:04'
figure_nz:
- title_l1: Age distribution of people working in the health and general insurance
    industry in New Zealand
  url: https://figure.nz/chart/YLD1eftMXZOMsBur-0HUU8uJplxJO1DRK
- title_l1: Age distribution of people working in the health care services industry
    (other) in New Zealand
  url: https://figure.nz/chart/YLD1eftMXZOMsBur-1TjybFLkyyv2kkoR
- title_l1: Age distribution of people working in the allied health services industry
    in New Zealand
  url: https://figure.nz/chart/YLD1eftMXZOMsBur-Js8hhZQc3mk6au17
- title_l1: Age distribution of people working in the medical and other health care
    services industry in New Zealand
  url: https://figure.nz/chart/YLD1eftMXZOMsBur-UsD6CTQInEADyxnj
- title_l1: People employed in the medical and other health care services industry
    in New Zealand who are also studying
  url: https://figure.nz/chart/zi0htbI6Pqc0N4rn-HMAN7rJi6AaHEkRI
id: census_incomes_by_qualification_study_participation_age_and_industry_2013
layout: post
link: http://www.stats.govt.nz/Census/2013-census/data-tables.aspx
provider: Statistics New Zealand
tags:
- employment
- figure.nz
title: 'Census: Incomes by qualification, study participation, age and industry 2013'
---

<h4><u> More details on figure.nz</u></h4>
{% for item in page.figure_nz%}
<ul class="post-list">
    <li><a href="{{ item.url }}">{{ item.title_l1 }}</a></li>
{% endfor %}
</ul>