import pandas as pd

# Nomes dos arquivos de entrada
arquivo1 = 'medallion/silver/acidentes2025_tratado.csv'
arquivo2 = 'medallion/silver/datatran2025_tratado.csv'

# Nome do arquivo de saída
arquivo_saida = 'acidentes_totais_2025.csv'

# Carrega o primeiro arquivo CSV
try:
    df1 = pd.read_csv(arquivo1, sep=';', encoding='latin-1')
    print(f"Arquivo '{arquivo1}' carregado com {len(df1)} linhas.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo1}' não foi encontrado.")
    exit()

# Carrega o segundo arquivo CSV
try:
    df2 = pd.read_csv(arquivo2, sep=';', encoding='latin-1')
    print(f"Arquivo '{arquivo2}' carregado com {len(df2)} linhas.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo2}' não foi encontrado.")
    exit()

# Concatena os dois DataFrames (junta as linhas)
# O parâmetro 'ignore_index=True' redefine o índice para o novo DataFrame
df_combinado = pd.concat([df1, df2], ignore_index=True)

# Salva o DataFrame combinado em um novo arquivo CSV, usando o mesmo delimitador
df_combinado.to_csv(arquivo_saida, sep=';', index=False)