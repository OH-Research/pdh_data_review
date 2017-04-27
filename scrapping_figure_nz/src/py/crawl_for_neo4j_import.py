import scrapy, json

class FigureNzSpider(scrapy.Spider):
    name = "FigureNz" 

    def __init__(self, i_max="84", *args, **kwargs):
      """
      Loop other all preview health related pages containing charts, maps and tables.
      Default parameters is 84 but can be specified by user with the -a flag.
      """
      super(FigureNzSpider, self).__init__(*args, **kwargs)
      prefix = "https://figure.nz/search/?query=health&types=g,m,t&page="
      self.start_urls = [prefix + str(i) for i in range(1, int(i_max) + 1)]

    def parse(self, response):
      """
      Just parse the unreadable big json included in a script tag from the preview
      page. It seems to be an API response included in the page source as plain text.
      """
      api_response = response.xpath("//script[starts-with(@src, '/cdn/js/app-search_results')]/following::script/text()").extract_first()
      list_as_str = api_response.split("results: ", 1)[1].split("],", 1)[0] + "]"
      datasets = json.loads(list_as_str)
      n = len(datasets)
      urls = ["https://figure.nz/" + datasets[i]['_type'] + "/" + datasets[i]['_id'] for i in range(n)]
      titles = [datasets[i]['_source'].get('title', '') for i in range(n)]
      subtitles = [datasets[i]['_source'].get('subtitle', '') for i in range(n)]
      names = [datasets[i]['_source'].get('name', '') for i in range(n)]
      for (url, title, subtitle, name) in zip(urls, titles, subtitles, names):
          yield scrapy.Request(url, callback=self.parse_item, meta={'title': title, 'subtitle': subtitle, 'name': name, 'url': url})

    def parse_item(self, response):
      """
      Finaly parse an item page.
      """
      provider = response.xpath("//h4[text()='Data provided by']/following::p[1]/a/text()").extract_first()
      dataset = response.xpath("//h4[text()='Dataset name']/following::p[1]/text()").extract_first()
      tags = response.xpath("//div[@class='taglist']/ul/li/a/text()").extract()
      yield {'provider': provider, 'dataset': dataset, 'title': response.meta['title'], 'tags': "|".join(tags), 'name': response.meta['name'], 'subtitle': response.meta['subtitle'], 'url': response.meta['url']}
