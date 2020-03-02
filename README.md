# Craigslist Web Scraper
## David Eliason
### February 14, 2020

## Description
Use of python scrapy module to scrape craigslist data via API, then save to CSV formatted file for analysis later.

## Context
There are two types of data: structured and unstructured data. The latter is an increasing source of information given the rise of mobile devices globally, along with IoT, social media, and a wide variety of other sources of input.

Unstructured data can be approached for obtaining further information and insights, and can be used for image recognition, for AI applications such as Alexa, iPhone unlocking, auto drive, spam detection, monitoring social media. With unstructured data, we have massive amounts of data with increased potential for obtaining more information and a potential resultant of better decision making.

In this exercise, the first step is to import the unstructed data, which is done using a web scraping framework, called Scrapy, which we use to build a scraping tool. Python processes the returned data using this tool- features are extracted, in a movement towards more-structured data. Data analysis can then be done on this data, both descriptive, predictive. 

Scrapy is a Python module, which is imported into a Jupyter Notebook as an editor

## Steps
1. create project craigslist_web_scraping
2. create spider named 'rentals' and provide the craigslist url: https://seattle.craigslist.org/d/vacation%E2%80%90rentals/search/vac

3. edit spider so that it parses data nodes with class "result-title-hdrlnk"
4. $ scrapy crawl rentals 
- returns in terminal all the titles
5. add loop to change output from array to object with key-value pair
6. $ scrapy crawl jobs -o result-titles.csv
- send output to csv format

![Website Scraped Data Output](Scrapy_CSV_Ouput.png)

