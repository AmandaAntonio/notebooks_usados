import sqlite3
import pandas as pd

# Caminho para o banco de dados SQLite
db_filename = '../data/notebooks.db'

# Conectar ao banco de dados
conn = sqlite3.connect(db_filename)

# Carregar os dados em um DataFrame
df = pd.read_sql_query("SELECT * FROM notebooks", conn)

# Fechar a conexão
conn.close()

# Exibir as primeiras linhas do DataFrame
#print(df.head())

# Respondendo as perguntas

# 1.Preço médio dos notebooks
preco_medio = df['preco'].mean()
print(f'O preço médio dos notebooks é', preco_medio)

# 2.O notebook mais caro listado
mais_caro = df.loc[df['preco'].idxmax()]
print(f'O notebook mais caro é o', mais_caro)

# 3. O notebook mais barato listado
mais_barato = df.loc[df['preco'].idxmin()]
print(f'O notebook mais baroto é o ', mais_barato)

# 4.Preço médio por marca
preco_medio_marca = df[['marca', 'preco']].groupby('marca').mean().sort_values(by='preco', ascending=False)
print(preco_medio_marca)

# 5.A quantidade de notebooks listados por marca
marcas_pop = df['marca'].value_counts().sort_values(ascending=False)
print(marcas_pop)

# 6.A quantidade de notebooks listados por sistema operacional
sis_op_pop = df['sistema_operacional'].value_counts().sort_values(ascending=False)
print(sis_op_pop)

# 7.O preço médio dos notebooks baseados em seu sistema operacional
preco_medio_sis_op = df[['preco', 'sistema_operacional']].groupby('sistema_operacional').mean().sort_values(by='preco', ascending=False)
print(preco_medio_sis_op)

# 8.Preço médio de notebooks por tamanho da RAM.
preco_medio_ram = df[['preco', 'ram']].groupby('ram').mean().sort_values(by='preco', ascending=False)
print(preco_medio_ram)

# 9. Tamanho de memória RAM mais listada
ram_pop = df['ram'].value_counts().sort_values(ascending=False)
print(ram_pop)