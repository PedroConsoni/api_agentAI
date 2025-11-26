import sqlite3
import pandas as pd

df = pd.read_csv('medallion/gold/acidentes_totais_2025.csv', sep=';')

conversao = sqlite3.connect('./medallion/gold/acidentes_final.db')

df.to_sql(
    name='acidentes_final',
    con=conversao,
    if_exists='replace',
    index=False
)

conversao.close()