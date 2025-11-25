from google.adk.agents import Agent

root_agent = Agent(
    name="policial_federal",
    model="gemini-2.5-flash",
    description='''
    Voce e agenr da Policia Federal do Brasil. Sua funcao ver o conteudo de arquivos CSV relacionados a acidentes de transito no Brasil em 2025.
    Responda as perguntas com base no conteudo dos arquivos CSV disponiveis pelo get_csv. 
    '''
)