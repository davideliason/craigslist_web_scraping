# Craigslist Web Scraper
## David Eliason
### February 14, 2020

## Description
Use of python scrapy module to scrape craigslist data via API, then save to CSV formatted file for analysis later.

## Steps
1. create project craigslist_web_scraping
2. create spider named 'rentals' and provide the craigslist url: https://seattle.craigslist.org/d/vacation%E2%80%90rentals/search/vac

3. edit spider so that it parses data nodes with class "result-title-hdrlnk"
4. $ scrapy crawl rentals 
- returns in terminal all the titles
5. add loop to change output from array to object with key-value pair
6. $ scrapy crawl jobs -o result-titles.csv
- send output to csv format