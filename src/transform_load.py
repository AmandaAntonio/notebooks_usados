import os
import jsonlines
import pandas as pd
import sqlite3
import re

def extrair_informacoes(nome):
    # Inicializar variáveis
    marca, sistema_operacional, ram, processador, armazenamento_tipo, armazenamento_valor = None, None, None, None, None, None

    # Expressões regulares para extrair informações
    regex_marca = re.compile(r'^(Notebook|Chromebook) (\w+)')
    regex_processador = re.compile(r'(Intel Core \w\d \dª Gen|AMD \w+ \dª Gen)')
    regex_ram = re.compile(r'(\d+GB)')
    regex_sistema_operacional = re.compile(r'(Windows \d+|Chrome OS|Linux|Google)')
    regex_armazenamento = re.compile(r'(SSD|HD) (\d+GB)')

    # Extrair marca
    match = regex_marca.search(nome)
    if match:
        marca = match.group(2)
    
    # Extrair processador
    match = regex_processador.search(nome)
    if match:
        processador = match.group(1)
    
    # Extrair RAM
    match = regex_ram.search(nome)
    if match:
        ram = match.group(1)
    
    # Extrair sistema operacional
    match = regex_sistema_operacional.search(nome)
    if match:
        sistema_operacional = match.group(1)
    
    # Extrair armazenamento
    match = regex_armazenamento.search(nome)
    if match:
        armazenamento_tipo = match.group(1)
        armazenamento_valor = match.group(2)
    
    return marca, sistema_operacional, ram, processador, armazenamento_tipo, armazenamento_valor

def transformar_dados(dados):
    df = pd.DataFrame(dados)
    
    # Aplicar a função de extração de informações
    df[['marca', 'sistema_operacional', 'ram', 'processador', 'armazenamento_tipo', 'armazenamento_valor']] = df['nome'].apply(lambda x: pd.Series(extrair_informacoes(x)))

    # Limpar e transformar os dados de preço
    df['preco'] = df['preco'].str.strip()  # Remove espaços em branco no início e no final
    df['preco'] = df['preco'].str.replace(r'[^0-9,]', '', regex=True)  # Remove caracteres não numéricos exceto vírgula
    df['preco'] = df['preco'].str.replace(',', '.').astype(float)  # Substitui vírgula por ponto e converte para float

    # Limpar o nome do produto
    df['nome'] = df['nome'].str.strip()
    
    return df

def carregar_dados_no_sqlite(df, db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        df.to_sql('notebooks', conn, if_exists='replace', index=False)
        conn.close()
    except Exception as e:
        print(f"Erro ao carregar dados no SQLite: {e}")

if __name__ == "__main__":
    # Caminho do diretório 'data' um nível acima do diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, '..', 'data')
    
    # Caminho do arquivo JSONL
    jsonl_filename = os.path.join(data_dir, 'notebooks.jsonl')
    
    # Verificar se o arquivo JSONL existe
    if not os.path.exists(jsonl_filename):
        print(f"Arquivo JSONL não encontrado: {jsonl_filename}")
        exit(1)
    
    # Ler os dados do arquivo JSONL
    try:
        with jsonlines.open(jsonl_filename) as reader:
            dados = [obj for obj in reader]
    except Exception as e:
        print(f"Erro ao ler o arquivo JSONL: {e}")
        exit(1)
    
    # Transformar os dados
    df = transformar_dados(dados)
    
    # Caminho do banco de dados SQLite
    db_filename = os.path.join(data_dir, 'notebooks.db')
    
    # Carregar os dados no banco de dados SQLite
    carregar_dados_no_sqlite(df, db_filename)
    
    print(f"Dados transformados e salvos em {db_filename}.")
