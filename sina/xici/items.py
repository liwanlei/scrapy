# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field
import scrapy
class XiciItem(scrapy.Item):
	parent_title = Field()  
	parent_url = Field()  
	second_title = Field()  
	second_url = Field()  
	path = Field()  
	link_title = Field()
	link_url = Field() 
	head= Field() 
	content = Field()  
