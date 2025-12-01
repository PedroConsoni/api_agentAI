import sqlite3
from google.adk.agents import Agent

DB_PATH = "./medallion/gold/acidentes_final.db"

def consultar_banco(query: str):
    """
    Executa consultas SELECT no banco acidentes_final.db
    e retorna colunas e linhas de forma estruturada.
    
    Args:
        query: Comando SQL SELECT a ser executado
        
    Returns:
        dict: Dicionário com 'colunas' e 'linhas' ou 'erro'
    """
    query_lower = query.strip().lower()
    if not query_lower.startswith("select"):
        return {"erro": "Apenas consultas SELECT são permitidas por segurança."}
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        colunas = [d[0] for d in cursor.description] if cursor.description else []
        conn.close()
        return {"colunas": colunas, "linhas": rows}
    except sqlite3.Error as e:
        return {"erro": f"Erro no banco de dados: {str(e)}"}
    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}


def listar_tabelas():
    """
    Lista todas as tabelas disponíveis no banco SQLite.
    
    Returns:
        list ou dict: Lista de nomes de tabelas ou dicionário com erro
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
        """)
        tabelas = [t[0] for t in cursor.fetchall()]
        conn.close()
        return tabelas
    except sqlite3.Error as e:
        return {"erro": f"Erro ao listar tabelas: {str(e)}"}
    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}


def descrever_tabela(nome_tabela: str):
    """
    Retorna a estrutura (schema) de uma tabela específica.
    
    Args:
        nome_tabela: Nome da tabela a ser descrita
        
    Returns:
        list ou dict: Lista de colunas com seus tipos ou dicionário com erro
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({nome_tabela});")
        colunas = cursor.fetchall()
        conn.close()
        
        return [
            {
                "nome": col[1],
                "tipo": col[2],
                "nao_nulo": bool(col[3]),
                "padrao": col[4],
                "chave_primaria": bool(col[5])
            }
            for col in colunas
        ]
    except sqlite3.Error as e:
        return {"erro": f"Erro ao descrever tabela: {str(e)}"}
    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}


# ---------------------------------------------------------
# AGENTE CopRobo42
# ---------------------------------------------------------
root_agent = Agent(
    name="CopRobo42",
    model="gemini-2.5-flash",
    description=f"""
Você é o CopRobo42, agente especializado da Polícia Federal Brasileira em análise 
inteligente de dados de acidentes de trânsito. Sua missão é extrair insights valiosos 
dos dados para ajudar na prevenção de acidentes e elaboração de políticas públicas.

BANCO DE DADOS:
- Caminho: {DB_PATH}
- Contém dados consolidados sobre acidentes de trânsito no Brasil

FERRAMENTAS DISPONÍVEIS:
1. consultar_banco(query) - Executa consultas SQL SELECT
2. listar_tabelas() - Lista todas as tabelas disponíveis
3. descrever_tabela(nome) - Mostra estrutura de uma tabela específica

MODO DE OPERAÇÃO:
1. Quando receber uma pergunta, primeiro entenda o que o usuário precisa
2. Use listar_tabelas() e descrever_tabela() para conhecer a estrutura dos dados
3. Construa queries SQL SELECT otimizadas para extrair as informações necessárias
4. Analise os resultados e formule uma resposta clara e objetiva
5. NUNCA mostre código SQL ou processos internos ao usuário
6. NUNCA invente dados - use apenas o que está no banco
7. Apresente apenas a resposta final em linguagem natural, clara e profissional

FORMATO DE RESPOSTA:
- Use linguagem objetiva e profissional
- Apresente números e estatísticas de forma clara
- Quando relevante, forneça contexto e insights
- Se houver dados insuficientes, seja honesto sobre as limitações
- Organize informações complexas em parágrafos estruturados

ESPECIALIDADES:
- Análise de padrões e tendências de acidentes
- Identificação de fatores de risco
- Estatísticas por região, período, tipo de veículo, etc.
- Correlações entre condições (clima, horário, via) e gravidade
- Sugestões baseadas em dados para prevenção

Sempre mantenha postura profissional, ética e comprometida com a segurança pública.
"""
)