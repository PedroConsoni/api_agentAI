***The README you are accessing is in Portuguese-BR, if you prefer to access the README in English, [click here](README.md)***

# Projeto: Pipeline de Dados da PRF + Agente de IA com SQLite

Este projeto implementa um pipeline completo de **ETL (Extract, Transform, Load)** utilizando dados públicos da Polícia Rodoviária Federal (PRF), finalizando com a criação de um **agente de Inteligência Artificial** capaz de responder perguntas sobre os dados armazenados. Além disso, gráficos e análises são gerados automaticamente com base nas informações tratadas.

---

## Etapas do Projeto

### 1. Extração dos Dados da PRF

Realizei a coleta dos dados públicos disponibilizados pela PRF, obtendo arquivos brutos que serviram como base para todo o pipeline.

---

### 2. Transformação dos Dados com Python e Pandas

Utilizei **Python** e a biblioteca **Pandas** para:

* Limpeza dos dados
* Normalização de colunas
* Remoção de inconsistências
* Conversão para formatos adequados
* Preparação para armazenamento em banco

Essa etapa garantiu a qualidade e padronização dos dados antes da carga.

---

### 3. Carga dos Dados no SQLite

Após a transformação, os dados foram carregados para um banco **SQLite**, permitindo consultas rápidas e eficientes diretamente em um arquivo local `.db`.

---

### 4. Criação de um Agente de IA

Com os dados estruturados no SQLite, desenvolvi um **agente de Inteligência Artificial** capaz de:

* Ler o banco de dados
* Interpretar consultas do usuário
* Gerar respostas com base nos registros armazenados

Esse agente funciona como uma camada inteligente sobre o banco, permitindo perguntas em linguagem natural.

---

### 5. Geração de Gráficos e Análises

Implementei scripts que utilizam Python para:

* Analisar os dados diretamente no SQLite
* Gerar gráficos informativos com base nas consultas
* Responder perguntas visualmente, facilitando a interpretação das informações

Utilizei bibliotecas como **Matplotlib** e **Pandas** para as visualizações.

---

## Tecnologias Utilizadas

* Python
* Pandas
* SQLite
* Matplotlib
* Ferramentas de IA (ADK / modelo escolhido)

---

## Objetivo do Projeto

Criar um fluxo completo que demonstre práticas de engenharia de dados, análise e inteligência artificial, tudo baseado em dados reais e utilizando uma abordagem didática, robusta e bem estruturada.
