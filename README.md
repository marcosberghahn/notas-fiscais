# notas-fiscais
Streamlit App to view supermarket historic purchases and monitor the inflation perceived through personal price history


# Setup
1. pipenv shell
2. pipenv install streamlit
3. pipenv install pandas
4. pipenv install scrapy
4.1. scrapy startproject notasFiscaisScraper
4.2. scrapy genspider berghahn berghahn.com.br


# Run
1. pipenv shell
2. streamlit run streamlit_app.py
