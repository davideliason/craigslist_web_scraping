# -*- coding: utf-8 -*-
# \1. Title
# 2. Posted Date
# 3. Rental Price
# 4. Number of bedrooms
# 5. Neighborhood
# 6. Ad Text Content (description)

import scrapy
from scrapy import Request


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
            price = rental.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract()
            rooms = rental.xpath('span[@class="result-meta"]/span[@class="housing"]/text()').extract()
            neighborhood = rental.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            relative_url = rental.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
           
            
            

            yield Request(absolute_url, callback=self.parse_page, meta={'URL': absolute_url, 'Title': title, 'Posted Date':result_date, 'Rental Price': price, 'Number of Bedrooms': rooms, 'Neighborhood' : neighborhood})
           
    
    def parse_page(self, response): 
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract()) 
        response.meta['Description'] = description
        yield response.meta

        
        
            
 




            
 
      
 