# Jekyll Tipue Search

Full-text search in Jekyll using Tipue Search. No plugin necessary.

## Installation

1. Add the `assets/tipuesearch` folder and all contents to the Jekyll assets folder, usually this is `assets`.

2. Add the following to the head template, usually `_includes/head.html`:

  ```
  {% if page.title == "Search" %}
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
  <script type="text/javascript" src="{{ "/assets/tipuesearch/tipuesearch_content.js" | relative_url }}"></script>
  <link rel="stylesheet" type="text/css" href="{{ "/assets/tipuesearch/tipuesearch.css" | relative_url }}">
  <script type="text/javascript" src="{{ "/assets/tipuesearch/tipuesearch_set.js" | relative_url }}"></script>
  <script type="text/javascript" src="{{ "/assets/tipuesearch/tipuesearch.min.js" | relative_url }}"></script>
  {% endif %}
  ```

3. Add the example search page `search.html` to the site.

## Usage

Jekyll will use the Liquid code in `tipuesearch/tipuesearch_content.js` to generate a search index. The form in `search.html` uses Javascript to search the index and display a list of results.

Refer to the [Tipue Search documentation](http://www.tipue.com/search/docs/) for available configuration options for the search form and display of search results.

### Including pages and collections

By default, only posts are included in the search index. Pages and collections are not included.

Add the following to `_config.yml` to include pages and collections. `collections` is an array containing a list of collections to be included:

```
tipue_search:
  include:
    pages: true
    collections: [apples, oranges]
```

### Excluding from search index

Exclude single documents from the search index with a front-matter variable:

```
exclude_from_search: true
```

Exclude multiple files, tags or categories using a setting in `_config.yml`. `files` is an array containing a list of file paths to be excluded. `tags` and `categories` are arrays containing lists of tags and categories to be excluded:

```
tipue_search:
  exclude:
    files: [search.html, _apples/gragg.md, _oranges/valencia.md]
    tags: [tag1, tag2]
    categories: [category1, category2]
```

## Support

[Open an issue](https://github.com/xHN35RQ/jekyll-tipue-search/issues) if you have any problems, questions or suggestions for improvement.
