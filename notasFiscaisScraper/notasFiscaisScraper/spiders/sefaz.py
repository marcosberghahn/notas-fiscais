import scrapy


class SefazSpider(scrapy.Spider):
    name = 'sefaz'
    # allowed_domains = ['berghahn.com.br']
    start_urls = ['http://berghahn.com.br/']

    def parse(self, response):
        title = response.css('.NFCCabecalho_SubTitulo')
        headline = response.css('.framer-styles-preset-3nqyhf')
        # for itens in response.css ('#respostaWS > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(5) > td > table > tbody > tr'):
            # 'item' : 
        pass
