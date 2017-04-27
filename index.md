---
layout: home
tipue_search_active: true
exclude_from_search: true
---

{% capture tags %}
  {% for tag in site.tags %}
    {{ tag[1].size | plus: 1000 }}#{{ tag[0] }}#{{ tag[1].size }}
  {% endfor %}
{% endcapture %}

<ul class="tag-box inline">
{% assign sortedtags = tags | split:' ' | sort %}
{% for tag in sortedtags reversed %}
    {% assign tagitems = tag | split: '#' %}
    <li><a href="#{{ tagitems[1] }}">{{ tagitems[1] | capitalize }}  (<span>{{ tagitems[2] }}</span>)</a></li>
{% endfor %}
</ul>

{% for tag in site.tags %} 
  <h2 id="{{ tag[0] }}">{{ tag[0] | capitalize }}</h2>
  <ul class="post-list">
    {% assign pages_list = tag[1] %}  
    {% for post in pages_list %}
      {% if post.title != null %}
      {% if group == null or group == post.group %}
      <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endif %}
      {% endif %}
    {% endfor %}
    {% assign pages_list = nil %}
    {% assign group = nil %}
  </ul>
{% endfor %}
