# -*- coding: utf-8 -*-
import scrapy


class RentalsSpider(scrapy.Spider):
    name = 'rentals'
    allowed_domains = ["craigslist.org"]
    start_urls = ['https://seattle.craigslist.org/d/vacation%E2%80%90rentals/search/vac/']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        
        for title in titles:
            yield {'Title': title}
 