import requests
from bs4 import BeautifulSoup
import pandas as pd


class scrap:
        def __init__(self):
                self.url = 'https://lista.mercadolivre.com.br/'
                self.produto_busca = input('Qual produto você busca? ')
                self.response = requests.get(self.url + self.produto_busca) 
                self.site = BeautifulSoup(self.response.text, 'html.parser')
                self.produtos = self.site.find_all('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core ui-search-result--advertisement andes-card--padding-default andes-card--animated'})
                self.lista = []
                
        def Iniciar(self):
               self.achar_intens_e_printar() 
               
                
        
        def achar_intens_e_printar(self):
                for self.produto in self.produtos:
                        self.titulo = self.produto.find('h2', attrs={'class': 'ui-search-item__title'})
                        self.link = self.produto.find('a', attrs={'class': 'ui-search-link'})
                        self.preco_inteiro = self.produto.find('span', attrs={'class':'price-tag-fraction' })
                        self.preco_centavos = self.produto.find('span', attrs={'class': 'price-tag-cents'})
                        self.lista.append([self.titulo.text, self.preco_inteiro.text, self.link['href']])
                        self.frame_pandas = pd.DataFrame(self.lista, columns=['Título','Preço', 'Link'])
                        self.frame_pandas.to_excel('5_resultados.xlsx', index=False)


       
                





comecar = scrap()
comecar.Iniciar()