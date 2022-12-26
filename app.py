import streamlit as st
import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
# from notasFiscaisScraper.notasFiscaisScraper.spiders import BerghahnSpider

def main():
    st.set_page_config(page_title="Notas Fiscais", page_icon="🧾", layout="wide", initial_sidebar_state="auto")
    """
    # Análise de Notas Fiscais

    1. Receber nota por webhoock
    
    2. Fazer Scrapping das notas
    
    3. Processar dados brutos das notas
    
    4. Salvar dados processados
    
    5. Montar Dashboards

    Nota demo: https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p=43221293015006003724651270000808751178834500|2|1|1|6307B5F26979151787F505295212EE8D57F23893

    """
    
    nota_demo = "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p=43221293015006003724651270000808751178834500|2|1|1|6307B5F26979151787F505295212EE8D57F23893"
    st.text_input("URL da nota", placeholder=nota_demo, key="notaURL")

    if st.button("Importar nota", type="primary"):
        scrapper(st.session_state.notaURL)



class BerghahnSiteSpider(scrapy.Spider):
    name = 'berghahn'
    # allowed_domains = ['berghahn.com.br']
    start_urls = ['http://berghahn.com.br/']

    def parse(self, response):
        title = response.css('title ::text').get()
        # headline = response.css('.framer-styles-preset-3nqyhf')
        yield {
            'title': response.css('title ::text').get(),
            'headline': response.css('.framer-styles-preset-3nqyhf ::text').get()
            # 'partial': response.css('.framer-styles-preset-3nqyhf ::text').get()[8:13],
            # 'purpose': response.css('.framer-styles-preset-3nqyhf ::text').get()[13:]
        }
        # return title


def scrapper(url):
    # scrapy crawl berghahn -O berghahn.json
    # retorno = berghahn.BerghahnSpider("http://berghahn.com.br")
    # st.json(retorno)
    # scrapy.Spider.BerghahnSpider
    # response = ""
    # scrapy.shell
    # scrapy.fetch(url)
    # response

    # process = CrawlerProcess()
    # retorno = process.crawl(BerghahnSiteSpider)    
    # st.write(retorno)

    # retorno2 = BerghahnSiteSpider.parse('http://berghahn.com.br',response="")
    # st.write(retorno2)
    # st.json(retorno2)
    # with st.spinner:
    
    # st.json(retorno)
    
    process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(BerghahnSiteSpider)
    # process.start() # the script will block here until the crawling is finished

    
    
if __name__ == "__main__":
    main()