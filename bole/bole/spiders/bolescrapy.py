# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from bole.items import BoleItem

class BolescrapySpider(scrapy.Spider):
    name = 'bolescrapy'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']
    def parse(self, response):
        item=BoleItem()
        post_list=response.xpath('//div[@class="grid-8"]')
        for post in post_list:
        	item['title']=post.xpath('.//div[@class="post-meta"]/p/a[1]/text()').extract()
        	item['lei']=post.xpath('.//div[@class="post-meta"]/p/a[2]/text()').extract()
        	yield item
