---
layout: default
multiple_select_active: true
tipue_search_active: true
exclude_from_search: true
--- 

{% capture provider_list %}{% for post in site.posts %}#{{ post.provider }}{% endfor %}{% endcapture %}
{% assign provider_array = provider_list | split:'#' | uniq %}

{% capture tag_list %}{% for post in site.posts %}{% for tag in post.tags %}#{{ tag }}{% endfor %}{% endfor %}{% endcapture %}
{% assign tag_array = tag_list | split:'#' | uniq %}

<!-- other solution

{% capture tag_list %}{% for tag in site.tags %}#{{ tag | first }}{% endfor %}{% endcapture %}
{% assign tag_array = tag_list | split:'#' | uniq %}

-->


<div id="datasets">

<table>
   <!-- sorting/filtering control row, need to be out of the tbody tag -->
    <tr> 
    <td width="50%"> 
       <button class="sort" data-sort="name">sort</button>
       <input class="search-name" placeholder="search" />     
    </td> 
    <td width="25%"> 
         <button class="sort" data-sort="provider">sort</button>
         <select name="filter-provider" id="filter-provider" class="filter-provider" style="width: 150px;" multiple="multiple">
       {% for provider in provider_array %}
         {% if provider.size > 0 %} <option value="{{ provider }}" selected>{{ provider }}</option>{% endif %}
       {% endfor %}
       </select>
    </td>
    <td width="25%"> 
         <select name="filter-tag" id="filter-tag" class="filter-tag" style="width: 150px;" multiple="multiple">
       {% for tag in tag_array %}
         {% if tag.size > 0 %} <option value="{{ tag }}" selected>{{ tag }}</option>{% endif %}
       {% endfor %}
       </select>
    </td>
    </tr>
   <!-- actual content of the list -->
    <tbody class="list">
  	{% for post in site.posts %}
    <tr>
    	<td width="50%" class="name"><a class="post-link" href="{{ post.url | relative_url }}"><font size="2">{{ post.title | truncate: 80 }}</font></a></td>
        <td width="25%" class="provider"><font size="2">{{ post.provider }}</font></td>
        <td width="25%" class="tags">{% for tag in post.tags %}<a class="tag-link" href="{{ site.url }}/pdh_data_review/topics/#{{ tag }}">#{{ tag }}</a> {% endfor %}</td> 
    </tr>
    {% endfor %}

    </tbody>
 </table>

</div>

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src="assets/list.min.js"></script>
<script src="assets/multiple-select.js"></script>

<script>

// define the dropdown multiselect controls
$('#filter-tag').multipleSelect({name: 'tag', 
                                 filter: true,
                                 onClose: function() { // update providers selection when close (mimic excel behavior)
                                         var provider_list = datasetList.matchingItems.map(function(a) {return a._values['provider'].match(/>(.*?)</)[1];});
                                         $('#filter-provider').multipleSelect('setSelects', provider_list);
                                }});

$('#filter-provider').multipleSelect({name: 'provider',
                                     filter: true,
                                      onClose: function() { // update tags selection when close (mimic excel behavior)
                                            var tag_list = datasetList.matchingItems.map(function(a) {return a._values['tags'].match(/>#(.*?)</g);}); // extract >#tag<
                                            tag_list = [].concat.apply([], tag_list).map(function(a) {return a.match(/[a-zA-Z|\-|\.]+/g);}); // extract tag
                                            tag_list = [].concat.apply([], tag_list); // build the array
                                            $('#filter-tag').multipleSelect('setSelects', tag_list);
                                }});

// define the dynamic list
var options = {
  valueNames: [ 'name', 'provider', 'tags' ]
};

var datasetList = new List('datasets', options);

// set up the search control on dataset names
$('.search-name').on('keyup', function() {
  var searchString = $(this).val();
  datasetList.search(searchString, ['name']);
});

// make sure that the filter matches provider and tag condition
function filterCondition(item) {
    var selection_provider = $('.filter-provider').val();
    var selection_tag = $('.filter-tag').val();
    var provider = item.values().provider.match(/>(.*?)</)[1]; // because of the font tag we need a regex to extract the actual value
    var tags = item.values().tags;
    return (selection_tag != null && 
            selection_provider != null && 
            selection_provider.indexOf(provider) != -1 && 
            selection_tag.some(function(v) { return tags.indexOf(v) >= 0;}));
}

// set up the filtering control on dataset providers - make sure that the filter matches provider and tag condition
// we use the click event rather than change to make sure the user is actually using the control (not an update on a close event)
$('.filter-provider').on('click', function () { 
     datasetList.filter(function(item) {
     	  return filterCondition(item); 
    });
});

// set up the filtering control on dataset tags - make sure that the filter matches provider and tag condition
// we use the click event rather than change to make sure the user is actually using the control (not an update on a close event)
$('.filter-tag').on('click', function () { 
     datasetList.filter(function(item) {
        return filterCondition(item); 
    });
});



</script>
