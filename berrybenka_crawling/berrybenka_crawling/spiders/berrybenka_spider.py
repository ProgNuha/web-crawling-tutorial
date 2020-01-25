import scrapy

class BerryBenkaSpider(scrapy.Spider):
    name = 'products'
    start_urls = [
        'https://berrybenka.com/clothing/outerwear/women'
    ]

    def parse(self, response):
        product_name = response.css('div.detail-left').css('h1::text').getall()
        # product_price = response.css('.discount::text').getall()
        # product_image = response.css('.catalog-image').css('img::attr(src)').getall()
        yield {'product': product_name}
