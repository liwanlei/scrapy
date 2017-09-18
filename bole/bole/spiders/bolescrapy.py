# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from bole.items import BoleItem
import re
from urllib import parse
class BolescrapySpider(scrapy.Spider):
    name = 'bolescrapy'
    allowed_domains = ['blog.jobbole.com']
    def start_requests(self):
        x=0
        for x in range(1,78):
            x+=1
            url='http://python.jobbole.com/all-posts/page/'+str(x)
            yield Request(url)
    def parse(self, response):
        item=BoleItem()
        posts=response.xpath('//div[@class="grid-8"]/div')
        for post in posts:
        	item['title']=post.xpath('.//div[@class="post-meta"]/p/a[1]/text()').extract()
        	item['lei']=post.xpath('.//div[@class="post-meta"]/p/a[2]/text()').extract()
        	item['title_url']=post.xpath('.//span[@class="read-more"]/a/@href').extract()
        	item['post_desc']=post.xpath('.//span[@class="excerpt"]/p/text()').extract()
        	if item=='':
                    break
        	yield item
        
