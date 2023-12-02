# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EfunItem(scrapy.Item, scrapy.Field):
    # define the fields for your item here like:
    # name = scrapy.Field()
    program = Field()
    barcode = Field()
    days = Field()
    times = Field()
    dates = Field()
    location = Field()
    classes = Field()
    avail = Field()


