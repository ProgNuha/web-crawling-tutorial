import scrapy
from ..items import Exercise1Item

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = Exercise1Item()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').get()
            author = quotes.css('.author::text').get()
            tag = quotes.css('.tag::text').get()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
