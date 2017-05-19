# coding:utf-8
# date: 2017年 05月 18日 星期四 18:03:53 CST

import scrapy

# usage: scrapy crawl quotesDemo_complex -o xxx.jl

class QuotesSpiderComplex(scrapy.Spider):
	name = "quotesDemo_complex"

	start_urls=[
		"http://quotes.toscrape.com/page/1/",
	]

	def parse(self, response):
		for quote in response.css('div.quote'):
			yield {
				'text' : quote.css ('span.text::text').extract_first (),
				'author': quote.css ('span small.author::text').extract_first (),
				'tags' : quote.css('div.tags a.tag::text').extract()

			}
		next_page = response.css('li.next a::attr(href)').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page,callback=self.parse)
