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
* Preço médio por marca
* A quantidade de notebooks listados por marca
* A quantidade de notebooks listados por sistema operacional
* O preço médio dos notebooks baseados em seu sistema operacional
* Preço médio de notebooks por tamanho da RAM
* Tamanho de memória RAM mais listada

## ETAPAS DO PROJETO

* Extrair dados do site da loja armazém de usados usando python, requests e beautiful soup.
* Transformar os dados usando python e pandas.
* Carregar os dados transformados no banco de dados SQLite3.
* Análise de dados para responder as perguntas de negócio.


## DIRETÓRIOS E ARQUIVOS:
    notebooksusados/
    src/: Diretório para os scripts de extração, transformação e carga.

        scraper.py: Contém o script de extração.

        transform_load: Contém o script de transformação e carga dos dados no SQLite.

        analysis.py: Contém o script de análise de dados para responder as perguntas de negócio.

    data/: Diretório para salvar os dados.

        notebooks.jsonl: Dados extraídos em formato JSONL.

        notebooks.db: Banco de dados SQLite.


    README.md: Instruções sobre o projeto.

    requirements.txt: Lista de dependências do projeto.

    .gitignore: Arquivo de texto que diz ao Git os arquivos ou pastas ele deve ignorar.

## COMO USAR

Executar a raspagem de dados
```bash
python scraper.py
````

Executar a transformação e carga
````bash
python transform_load.py
````

Executar a análise de dados
````bash
python analysis.py
````

## RESPOSTAS DAS PERGUNTAS DE NÉGOCIO.

* O preço médio dos notebooks é de R$ 1617.71

* O notebook mais caro é Notebook Dell Latitude E3530 custando R$2090.00

* O notebook mais barato é oChomeBook Samsung 500C Ram 2gb HD 16GB custando 799,90

* O preço médio por marca: Dell R$ 1.723.61, Lenovo R$ 1.573.33, HP R$ 1.520.76 e Acer R$ 1.190.00.

* Quantidade de notebooks listados por marca: Dell 36, HP 15, Lenovo 12, Acer 1.

* Sistema Operacional mais listado: Windows 10 está presente em 41 notebooks listados.

* Preço médio por sistema operacional:  Windows 11 R$ 1.812.17, Windows 10 RS 1.539.00.

* Preço médio dos notebooks pelo tamanho da memória RAM: 6gb R$ 1.990.00, 8gb R$ 1.640.31, 4gb 1.190.00.

* O tamanho da memória RAM mais listada é 8gb presente em 60 notebooks.
