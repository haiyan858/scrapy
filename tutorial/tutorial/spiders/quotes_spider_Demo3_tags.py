# coding:utf-8
import scrapy

# 网页首页的网址
# http://quotes.toscrape.com/
# http://quotes.toscrape.com/page/2/

# 抓取tag标签的text的url形如：
# http://quotes.toscrape.com/tag/inspirational/page/1/
# http://quotes.toscrape.com/tag/inspirational/

# usage: scrapy crawl quotesDemo_tag -o quotes-XXX.json -a tag=humor

class QuotesSpiderTags(scrapy.Spider):
	name = "quotesDemo_tag"

	def start_requests(self):
		url = 'http://quotes.toscrape.com/'

		# 'QuotesSpiderTags'object attribute 'tag_one'
		tag = getattr (self, 'tag_one')

		if tag is not None:
			url = url + 'tag/' + tag
			yield scrapy.Request(url,self.parse)

	def parse(self, response):
		for quote in response.css('div.quote'):
			yield {
				'text' : quote.css('span.text::text').extract_first(),
				'author' : quote.css('span small.author::text').extract_first(),
			}

		next_page = response.css('li.next a::attr(href)').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page,self.parse)

