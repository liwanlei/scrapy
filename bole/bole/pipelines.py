# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class hello(object):
	def __init__(self):
		self.coon=sqlite3.connect('dd.sqlite')
		self.cursul=self.coon.cursor()
	def process_item(self, item, spider):
		self.cursul.execute('insert into beijing(title,url,lei,miaoshu) values ("%s","%s","%s","%s")'%(item['title'],item['title_url'],item['lei'],item['post_desc']))
		self.coon.commit()
		# self.coon.close()
		return item
