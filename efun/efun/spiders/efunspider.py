import scrapy


class EfunspiderSpider(scrapy.Spider):
    name = "efunspider"
    allowed_domains = ["www.toronto.ca"]
    start_urls = ["https://www.toronto.ca/data/parks/prd/skating/reg/learn/index.html"]

    def parse(self, response):
        pass
