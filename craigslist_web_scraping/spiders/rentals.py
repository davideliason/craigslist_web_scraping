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
       
        #titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        
        #for title in titles:
        #    yield {'Title': title}
        rentals = response.xpath('//p[@class="result-info"]')
        
        for rental in rentals:
            title = rental.xpath('a/text()').extract_first()
            result_date = rental.xpath('time[@class="result-date"]/text()').extract()
            
            yield{'Title': title,
                 'Date':result_date}
            
 
      
 