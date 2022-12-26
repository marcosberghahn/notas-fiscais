import scrapy


class BerghahnSpider(scrapy.Spider):
    name = 'berghahn'
    # allowed_domains = ['berghahn.com.br']
    start_urls = ['http://berghahn.com.br/']

    def parse(self, response):
        # title = response.css('title')
        # headline = response.css('.framer-styles-preset-3nqyhf')
        # yield {
        #     'title': response.css('title ::text').get(),
        #     'headline': response.css('.framer-styles-preset-3nqyhf ::text').get(),
        #     'partial': response.css('.framer-styles-preset-3nqyhf ::text').get()[8:13],
        #     'purpose': response.css('.framer-styles-preset-3nqyhf ::text').get()[13:]
        # }
        return response.css('title ::text').get()

