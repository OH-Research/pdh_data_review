---
layout: post
provider: "dummy"
id: "dummy"
title: "dummy"
link: "dummy"
date:   2017-02-20 12:27:31 -0800
categories: non-new-zealand amazon-web-services
tags:
  - genomics
figure_nz:
  - item
---

<h4><u> More details on figure.nz</u></h4>
{% for item in page.figure_nz%}
<ul class="post-list">
    <li><a href="{{ item.url }}">{{ item.title_l1 }}</a></li>
{% endfor %}
</ul>
