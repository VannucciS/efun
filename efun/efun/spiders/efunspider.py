import scrapy


class EfunspiderSpider(scrapy.Spider):
    name = "efunspider"
    allowed_domains = ["www.toronto.ca"]
    start_urls = ["https://efun.toronto.ca/torontofun/Activities/ActivitiesDetails.asp?ProcessWait=N&aid=9936"]
    #["https://www.toronto.ca/data/parks/prd/skating/reg/learn/index.html"]

    def parse(self, response):

        entries = response.css('#activity-course-row')
        for entry in entries:
            yield{
                'url':  entry.css('.text-bold a::attr(href)').get(),
                'barcode': entry.xpath('td[2]/text()').get(),
                'day': entry.xpath('td[3]/text()').get(),
                'initialTime': entry.xpath('td[4]/text()[1]').get(),
                'endTime': entry.xpath('td[4]/text()[2]').get(),
                'start' : entry.xpath('td[5]/text()[1]').get(),
                'finish' : entry.xpath('td[5]/text()[2]').get(),
                'location': entry.xpath('td[6]/a/@title').get()
            }
        

