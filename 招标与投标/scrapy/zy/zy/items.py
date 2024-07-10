# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZyItem(scrapy.Item):
    timu = scrapy.Field()
    shijian = scrapy.Field()
    neirong = scrapy.Field()

