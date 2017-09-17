# -*- coding: utf-8 -*-
# @Date    : 2017-09-17 10:43:39
# @Author  : leizi
import scrapy
from baidu.items import BaiduItem
from scrapy import Request
import re
class XiaoHuarSpider(scrapy.Spider):
	name = 'douban_movie_top250'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',}
	def start_requests(self):
		url = 'https://movie.douban.com/top250'
		yield Request(url, headers=self.headers)
	def parse(self, response):
		item = BaiduItem()
		movies = response.xpath('//ol[@class="grid_view"]/li')
		for movie in movies:
			item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
			item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
			item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
			item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re('(\d+)人评价')[0]
			item['daoyan']=movie.xpath('.//div[@class="bd"]/p/text()').extract()[0]
			item['bieming']=movie.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()').extract()
			item['url']=movie.xpath('.//div[@class="hd"]/a/@href').extract()[0]
			yield item
		next_url=response.xpath('//span[@class="next"]/a/@href').extract()
		if next_url:
			print(next_url)
			next_url='https://movie.douban.com/top250'+next_url[0]
			yield Request(next_url,headers=self.headers)