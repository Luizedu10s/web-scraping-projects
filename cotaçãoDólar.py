import requests
from bs4 import BeautifulSoup

# REQUISIÇÃO NO SERVIDOR
requisicao_server = requests.get("https://wise.com/br/currency-converter/dolar-hoje")
# MOSTRAR CONTEÚDO DA PÁGINA
pag = requisicao_server.content
# TRANSFORMAR ATRAVÉS DO BEAUTIFULSOP, POIS PARA UTILIZAR AS FERRAMENTAS DA BIBLIOTECA É NECESSÁRIO FAZER ESTA CONVERSÃO.
pag_html = BeautifulSoup(pag, "html.parser")
# BUSCANDO INFORMAÇÕES NA PÁGINA
cotacao = pag_html.find('h3', attrs={'class': 'cc__source-to-target'})
# ENTRANDO NO INPUT 
valor_cot = cotacao.find('span', attrs={'class': 'text-success'})
# ARMAZENANDO EM UMA VARIÁVEL EM FORMA DE TEXTO.
valor_dolar_final = valor_cot.text
# CONVERTENDO PARA FLOAT.
valor_float = float(valor_dolar_final)
# SAÍDA DE DADOS NO PRINT
print(f'\033[1;41;32mU$ 1 dólar equivale a R${valor_float:.2f} no dia de hoje.\033[m')
