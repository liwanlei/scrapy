# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class BoleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    post_desc=scrapy.Field()
    #date=scrapy.Field()
    lei=scrapy.Field()
    title_url=scrapy.Field()
    #title_text=scrapy.Field()
    #dianzan=scrapy.Field()
    #pinglun=scrapy.Field()
    #shoucang=scrapy.Field()
    pass
