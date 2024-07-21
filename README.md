# Expansão de Negócio com Notebooks Usados

## PROBLEMA FICTÍCIO

O CEO da TechTudo, uma empresa que vende notebooks novos na cidade de São Paulo, recebeu muitos pedidos de seus clientes para adicionar notebooks usados de qualidade como opção de compra na loja.

Então ele decidiu entrar nesse ramo de negócios para expandir os serviços que presta aos clientes.

Sua função é ajudá-lo a extrair dados sobre notebooks do site da loja armazém de usados referências neste negócio. 

O CEO disse que a maioria dos clientes está procurando notebooks usados por causa do custo-benefício. 

Por isso ele gostaria de ver as seguintes métricas:

* Preço médio dos notebooks
* O notebook mais caro listado
* O notebooks mais barato listado
* Preços médios das principais marcas
* As marcas mais populares
* A maioria dos notebooks listados por sistema operacional
* Qualquer outro insight que possa ser obtido a partir dos dados que ajude na tomada de decisões.


## ETAPAS DO PROJETO

* Extrair dados do site da loja armazém de usados usando python, requests e beautiful soup.
* Transformar os dados usando python e pandas.
* Carregar os dados transformados no banco de dados SQLite3.
* Relatório com as repostas das perguntas de negócio.
* Dashboard de dados usando Tableau.

## DIRETÓRIOS E ARQUIVOS:
    notebooksusados/
    src/: Diretório para os scripts de extração, transformação e carga.
        scraper.py: Contém o script principal de extração.

    data/: Diretório para salvar os dados.
        notebooks.jsonl: Dados extraídos em formato JSONL.

    README.md: Instruções sobre o projeto.

    requirements.txt: Lista de dependências do projeto.

    .gitignore: Arquivo de texto que diz ao Git os arquivos ou pastas ele deve ignorar.

## COMO USAR

Executar a raspagem de dados
```bash
python scraper.py
````