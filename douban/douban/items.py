# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking=scrapy.Field()
    movie_name=scrapy.Field()
    score=scrapy.Field()
    score_num=scrapy.Field()
    daoyan=scrapy.Field()
    bieming=scrapy.Field()
    url=scrapy.Field()