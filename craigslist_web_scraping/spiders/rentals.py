# -*- coding: utf-8 -*-
# \1. Title
# 2. Posted Date
# 3. Rental Price
# 4. Number of bedrooms
# 5. Neighborhood
# 6. Ad Text Content (description)

import scrapy


class RentalsSpider(scrapy.Spider):
    name = 'rentals'
    allowed_domains = ["craigslist.org"]
    start_urls = ['https://seattle.craigslist.org/d/vacation%E2%80%90rentals/search/vac/']

    def parse(self, response):
        rentals = response.xpath('//p[@class="result-info"]')
        # titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        # posted_dates = response.xpath('//time[@class="result-date"]/text()').extract()
        
       # for title in titles:
        #    yield {'Title': title}
            
       # for date in posted_dates:
       #     yield {'Time': date}
        print(rentals)
 