import requests
from bs4 import BeautifulSoup

# URL BASE PARA PODER BUSCAR NO SITE DO MERCADO LIVRE:
url_base = 'https://lista.mercadolivre.com.br/'
# INPUT PARA SABER O PRODUTO QUE O USUÁRIO QUER BUSCAR NO SITE:
nome_produto = input("Digite o nome do produto que você quer buscar: ")
# REQUISIÇÃO AO SITE, É SÓ CONCATENAR A URL BASE JUNTO AO NOME DO PRODUTO DIGITADO NO INPUT.
requisicao = requests.get(url_base + nome_produto)
# BUSCA POR PRODUTO ESPECÍFICO NO SITE.
pag_html = BeautifulSoup(requisicao.content, 'html.parser')
# BUSCAR DENTRO DO HTML
pag = pag_html.find('li', attrs={'class': 'ui-search-layout__item'})
# NOME DO PRODUTO DENTRO DO SITE
nome_no_site = pag.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'}).text
# PREÇO DO PRODUTO DENTRO DO SITE.
preco_produto = float(pag.find('span', attrs={'class': 'andes-money-amount__fraction'}).text)
print(f'\033[1;30;47m O produto {nome_no_site} custa: R${preco_produto} \033[m ')
