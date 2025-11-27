import sqlite3
from google.adk.agents import Agent

DB_PATH = "./medallion/gold/acidentes_final.db"

def consultar_banco(query: str):
    """
    Executa SELECT no banco acidentes_final.db
    e retorna colunas e linhas.
    """
    query_lower = query.strip().lower()
    if not query_lower.startswith("select"):
        return {"erro": "Apenas SELECT é permitido."}

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()
        colunas = [d[0] for d in cursor.description]

        conn.close()

        return {"colunas": colunas, "linhas": rows}

    except Exception as e:
        return {"erro": str(e)}


# ---------------------------------------------------------
# Função interna — Listar tabelas
# ---------------------------------------------------------
def listar_tabelas():
    """Retorna todas as tabelas do SQLite."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name NOT LIKE 'sqlite_%';
        """)

        tabelas = [t[0] for t in cursor.fetchall()]

        conn.close()
        return tabelas

    except Exception as e:
        return {"erro": str(e)}


# ---------------------------------------------------------
# AGENTE CopRobo42 (sem tools)
# ---------------------------------------------------------
root_agent = Agent(
    name="CopRobo42",
    model="gemini-2.5-flash",
    description=f"""
    Você é o CopRobo42, agente da Polícia Federal especializado em análise
    de acidentes de trânsito.

    Banco utilizado: {DB_PATH}

    Como funcionar:
    Gere consultas SQL SELECT quando precisar de dados.Para acessar o banco, chame a função interna consultar_banco().Para ver a estrutura, chame listar_tabelas().Nunca invente dados; tudo deve vir do SQLite.Não mostre para o usuário no chat o que voce está fazendo para encontrar a resposta,nem os códigos em sql, apenas mostre a resposta final.Sempre mostre a resposta final em formato de texto simples.
    """
)

 