import pandas as pd
import numpy as np

# --- 1. CARREGAMENTO DOS DADOS ---
df = pd.read_csv('medallion/bronze/datatran2025.csv', encoding='LATIN1', sep=';')
print("Arquivo 'datatran2025.csv' carregado com sucesso.")


# --- 2. DEFINIÇÃO DAS COLUNAS POR TIPO ---
# Colunas que são números decimais e usam vírgula "," como separador invés de "."
colunas_decimais = ['km', 'latitude', 'longitude']

# Colunas que são números inteiros
colunas_inteiros = [
    'pessoas', 'mortos', 'feridos_leves', 'feridos_graves',
    'ilesos', 'ignorados', 'feridos', 'veiculos'
]

# Colunas categóricas (o tipo "category" serve para otimizar a memória quando existem muitos valores repetidos em uma coluna, o Pandas cria um índice interno para armazenar cada dado)
colunas_categoricas = [
    'dia_semana', 'uf', 'br', 'municipio', 'causa_acidente',
    'tipo_acidente', 'classificacao_acidente', 'fase_dia',
    'sentido_via', 'condicao_metereologica', 'tipo_pista',
    'tracado_via', 'uso_solo', 'regional', 'delegacia', 'uop'
]


# --- 3. APLICAÇÃO DAS CONVERSÕES ---
## A - Tratamento de Colunas Decimais ("," para "." e para Float)
print("\n1/3: Tratando colunas decimais...")

for coluna in colunas_decimais:
    print(f"\nAntes do tratamento ({coluna}):")
    print(df[coluna].head(5))

    df[coluna] = df[coluna].astype(str).str.replace(',', '.', regex=False)
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

    print(f"\nDepois do tratamento ({coluna}):")
    print(df[coluna].head(5))
    print(f"Tipo final: {df[coluna].dtype}")
    print("\n----------------------------------------------------------------")



## B - Tratamento de colunas de números inteiros
print("\n2/3: Tratando colunas de contagem...")

for coluna in colunas_inteiros:
    print(f"\nAntes do tratamento ({coluna}):")
    print(df[coluna].head(5))

    df[coluna] = df[coluna].astype(str).str.replace(',', '.', regex=False)
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
    df[coluna] = df[coluna].round().astype(pd.Int64Dtype())

    print(f"\nDepois do tratamento ({coluna}):")
    print(df[coluna].head(5))
    print(f"Tipo final: {df[coluna].dtype}")
    print("\n----------------------------------------------------------------")



## C - Conversão para o tipo de data, categóricas e o tratamento dos valores nulos
print("\n3/3: Convertendo colunas de data e categoria...")

# Tratamento da coluna 'data_inversa'
print("\nAntes do tratamento (data_inversa):")
print(df['data_inversa'].head(5))

df['data_inversa'] = pd.to_datetime(df['data_inversa'], errors='coerce', format='%Y-%m-%d')

print("\nDepois do tratamento (data_inversa):")
print(df['data_inversa'].head(5))
print(f"Tipo final: {df['data_inversa'].dtype}")
print("\n----------------------------------------------------------------")


# Tratamento da coluna 'horario'
print("\nTratando a coluna de horário...")

print("\nAntes do tratamento (horario):")
print(df['horario'].head(5))

# 1. Remover espaços
df['horario'] = df['horario'].astype(str).str.strip()

# 2. Converter para datetime com formato fixo
df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S', errors='coerce').dt.time

print("\nDepois do tratamento (horario):")
print(df['horario'].head(5))
print(f"Tipo final: {df['horario'].dtype}")
print("\n----------------------------------------------------------------")


# Converte para o tipo 'Category'
for coluna in colunas_categoricas:
    print(f"\nAntes do tratamento ({coluna}):")
    print(df[coluna].head(5))

    df[coluna] = df[coluna].astype('category')

    print(f"\nDepois do tratamento ({coluna}):")
    print(df[coluna].head(5))
    print(f"Tipo final: {df[coluna].dtype}")
    print("\n----------------------------------------------------------------")



# Tratamento dos valores
for coluna in colunas_categoricas:
    df[coluna] = df[coluna].cat.add_categories("Não informado")
    df[coluna] = df[coluna].fillna("Não informado")


# --- 4. VERIFICAÇÃO FINAL ---
print("\n--- Verificação final do tratamento ---")

print("\nVerificando valores nulos:")
print(df.isna().sum())
print("\n----------------------------------------------------------------")

print("\nExibindo tipos finais das colunas:")
df.info()

df.to_csv('datatran2025_tratado.csv', encoding='LATIN1', index=False, sep=';')