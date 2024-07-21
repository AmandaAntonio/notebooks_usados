import os
import requests
from bs4 import BeautifulSoup
import jsonlines

def buscar_pagina(url, pagina):
    resposta = requests.get(url, params={'pg': pagina})
    resposta.raise_for_status()
    return resposta.content

def raspar_pagina(conteudo_html):
    site = BeautifulSoup(conteudo_html, 'html.parser')
    notebooks = site.findAll('a', attrs={'class':'info-product'})
    lista_notebook = []
    for notebook in notebooks:
        nome = notebook.find('div', attrs={'class':'product-name'}).text
        preco = notebook.find('span', attrs={'class':'price-off'}).text
        lista_notebook.append({'nome': nome, 'preco': preco})
    return lista_notebook

def paginacao(base_url, max_pages=10):
    todos_notebooks = []
    pagina = 1
    while pagina <= max_pages:
        print(f"Raspando a página {pagina}...")
        conteudo_html = buscar_pagina(base_url, pagina)
        notebooks = raspar_pagina(conteudo_html)
        if not notebooks:
            print("Não existem mais produtos. Fim da paginação.")
            break
        todos_notebooks.extend(notebooks)
        pagina += 1
    return todos_notebooks

def salvar_em_jsonl(data, filename):
    with jsonlines.open(filename, mode='w') as writer:
        writer.write_all(data)

if __name__ == "__main__":
    base_url = 'https://www.armazemdeusados.com.br/loja/catalogo.php?loja=1219750&categoria=61'
    todos_notebooks = paginacao(base_url)
    
    # Caminho do diretório data um nível acima do diretório atual
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    
    # Criar diretório 'data' se não existir
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Caminho do arquivo JSONL
    filename = os.path.join(data_dir, 'notebooks.jsonl')
    
    # Salvar dados em JSONL
    salvar_em_jsonl(todos_notebooks, filename)
    
    print(f"Dados extraídos e salvos em {filename}.")

