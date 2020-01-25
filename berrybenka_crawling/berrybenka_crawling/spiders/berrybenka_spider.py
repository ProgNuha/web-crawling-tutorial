import scrapy
from ..items import BerrybenkaCrawlingItem

class BerryBenkaSpider(scrapy.Spider):
    name = 'products'
    start_urls = [
        'https://berrybenka.com/clothing/outerwear/women'
    ]

    def parse(self, response):

        items = BerrybenkaCrawlingItem()

        products = response.css('#li-catalog')

        for product in products:
            title = product.css('div.detail-left').css('h1::text').get()
            price = product.css('.discount::text').get()
            source_image = product.css('.catalog-image').css('img::attr(src)').get()
            
            items['title'] = title
            items['price'] = price
            items['source_image'] = source_image

            yield items
