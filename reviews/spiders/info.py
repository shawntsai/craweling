

# -*- coding: utf-8 -*-
import scrapy
import datetime
import seaborn as sns


class InfoSpider(scrapy.Spider):
                       
    name = 'info'
    def start_requests(self):
        parent_urls = [
              # 'http://www.drb.ie/essays?page=', 
              # 'http://www.drb.ie/new-books?page=', 
              # 'http://the-american-interest.com/c/reviews/',
              'https://bookpage.com/reviews?page=', 
        ]
        
        bookpage_urls = []
        drb_urls = []
        urls = []

        # for i in range(1, 102):
            # drb_urls.append(parent_urls[0] + str(i))


        # for i in range(1,44):
            # drb_urls.append(parent_urls[1] + str(i))

        # for url in drb_urls:
            # yield scrapy.Request(url=url, callback=self.parseDrb)


        # for j in range(2, 38):
            # urls.append(parent_urls[2] + 'page/' + str(j) +'/')

        # for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)
        
 
        for i in range(2, 130):
            bookpage_urls.append(parent_urls[0] + str(i))

        for url in bookpage_urls:
            yield scrapy.Request(url=url, callback=self.parse_book_page)


     
    def parse_book_page(self, response):
        for next_page in response.css('h2 a::attr(href)').extract():
            if next_page is not None:
                next_page = 'https://bookpage.com' + next_page
                yield scrapy.Request(next_page, callback=self.output,cookies={'currency': 'USD', 'country': 'UY'}, meta={'dont_merge_cookies':True})

   
    def parse(self, response):
        for next_page in response.css('span.archive-title a::attr(href)').extract():
            if next_page is not None:
                yield scrapy.Request(next_page, callback=self.output,cookies={'currency': 'USD', 'country': 'UY'}, meta={'dont_merge_cookies':True})

    def parseDrb(self, response):
        for next_page in response.css('h1.sfitemTitle a::attr(href)').extract():
            if next_page is not None:
                next_page = 'http://www.drb.ie/' + next_page
                yield scrapy.Request(next_page, callback=self.output,cookies={'currency': 'USD', 'country': 'UY'}, meta={'dont_merge_cookies':True})

    def output(self, response):
        item = {} 
        item['author']= response.css('p.author-small a::text').extract_first()
        item['title']= response.css('h4::text').extract_first().lstrip("\n").rstrip("\n")

        item['genre']= response.css('.genre-links a::text').extract_first()
        item['reviewer']= response.css('.author-small a::text').extract()[4]
        # item['date']= response.css('.article-issue::text').extract_first()
        item['issue'] = response.css('h2::text').extract_first().lstrip("\n").rstrip("\n")
        yield item

