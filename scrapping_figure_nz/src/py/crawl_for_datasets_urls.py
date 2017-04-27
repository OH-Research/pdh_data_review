# scrapy runspider spider.py -o figure_nz_health.csv -a i_max=84 &> out.log

import scrapy, json

class FigureNzSpider(scrapy.Spider):
    name = "FigureNz" 

    def __init__(self, i_max="84", *args, **kwargs):
        super(FigureNzSpider, self).__init__(*args, **kwargs)
        prefix = "https://figure.nz/search/?query=health&types=g,m,t,t&page="
        self.start_urls = [prefix + str(i) for i in range(1, int(i_max) + 1)]

    def parse(self, response):
      api_response = response.xpath("//script[starts-with(@src, '/cdn/js/app-search_results')]/following::script/text()").extract_first()
      list_as_str = api_response.split("results: ", 1)[1].split("],", 1)[0] + "]"
      datasets = json.loads(list_as_str)
      n = len(datasets)
      urls = ["https://figure.nz/" + datasets[i]['_type'] + "/" + datasets[i]['_id'] for i in range(n)]
      pages = [i for i in range(n)]
      items = [datasets[i]['_source'].get('title', '') + " " + datasets[i]['_source'].get('subtitle', '') + " " + datasets[i]['_source'].get('name', '') for i in range(n)]
      for (url, page, item) in zip(urls, pages, items):
        yield scrapy.Request(url, callback=self.parse_item, meta={'item': item, 'page': url})

    def parse_item(self, response):
        source = response.xpath("//h4[text()='Dataset name']/following::p[1]/text()").extract_first()
        url = response.xpath("//h4[text()='Webpage:']/following::a[1]/@href").extract_first()
        how = response.xpath("//h4[text()='How to find the data:']/following::div[1]/text()").extract_first()
        yield {'figure_url': response.meta['page'], 'item': response.meta['item'], 'source': source, 'source_url': url, 'how': how}
