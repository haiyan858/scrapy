# coding:utf-8
# date: 2017年 05月 17日 星期三 15:35:10 CST

# Spider 是用户编写用于从单个网站(或者一些网站)爬取数据的类。

import scrapy


# Scrapy 为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，
# 并将 parse 方法作为回调函数(callback)赋值给了Request。
# Request 对象经过调度，执行生成 scrapy.http.Response 对象并送回给 spider parse() 方法。
# Scrapy 使用了一种基于 XPath 和 CSS 表达式机制: Scrapy Selectors


# XPath例子
# /html/head/title: 选择HTML文档中 <head> 标签内的 <title> 元素
# /html/head/title/text(): 选择上面提到的 <title> 元素的文字
# //td: 选择所有的 <td> 元素
# //div[@class="mine"]: 选择所有具有 class="mine" 属性的 div 元素

# 也可以使用CSS Selector来从网页中 提取数据
# 推荐使用XPath

# usage: scrapy crawl quotesDemo
# Spider arguments are passed through the crawl command using the -a option. For example:
# usage: scrapy crawl quotesDemo -a category=electronics
# usage: scrapy crawl quotesDemo -o xxx.json -a tag=humor

class QuotesSpider (scrapy.Spider):
	name = "quotesDemo"

	# def start_requests(self):
	# 	urls = [
	# 		"http://quotes.toscrape.com/page/1/",
	# 		"http://quotes.toscrape.com/page/2/",
	# 	]
	# 	for url in urls:
	# 		yield scrapy.Request(url=url, callback=self.parse)

	# 上下两种写法是效果是相同的

	start_urls = [
		"http://quotes.toscrape.com/page/1/",
		"http://quotes.toscrape.com/page/2/",
	]

	# def parse(self, response):
	# 	page = response.url.split ("/")[-2]
	# 	filename = 'quotes-%s.html' % page
	# 	with open (filename, 'wb') as f:
	# 		f.write (response.body)
	# 	self.log ('---->Saved file %s' % filename)

	def parse(self, response):
		for quote in response.css ("div.quote"):
			yield{
				'text' : quote.css ("span.text::text").extract_first (),
				'author' : quote.css ("small.author::text").extract_first (),
				'tags' : quote.css ("div.tags a.tag::text").extract (),
			}



