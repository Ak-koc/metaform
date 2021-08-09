import scrapy
from scrapy import Request
import urllib
from datetime import datetime

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_unmanned_aerial_vehicles'
    ]

    def parse(self, response):

        for url in response.xpath('//div[@class="mw-parser-output"]/ul/li/a/@href'):
            href = response.urljoin(url.extract())
            yield scrapy.Request(href, callback=self.parse_page)

    def parse_page(self, response):

            title = response.css('.mw-headline::text').extract()
            text = response.css('p::text').extract()
            link = response.url
            date = datetime.now()
            items = {
                'date' : date,
                'link' : link,
                'title': title,
                'texts': text
            }
            yield items
