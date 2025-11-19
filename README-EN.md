***O README que você está acessando está em inglês, caso prefira acessar o README em Português-BR, [clique aqui](README.md)***

# Project: PRF Data Pipeline + AI Agent with SQLite

This project implements a complete **ETL (Extract, Transform, Load)** pipeline using public data from the Brazilian Federal Highway Police (PRF). It concludes with the creation of an **Artificial Intelligence agent** capable of answering questions based on the stored data.
Additionally, the project generates charts and visual analyses using the processed information.

---

## Project Stages

### 1. Extracting PRF Data

I collected the public datasets provided by PRF, obtaining the raw files that serve as the foundation of the entire pipeline.

---

### 2. Transforming Data with Python and Pandas

Using **Python** and **Pandas**, I performed the following transformations:

* Data cleaning
* Column normalization
* Removal of inconsistencies
* Conversion to structured formats
* Preparation for database loading

This step ensures data quality and consistency before inserting it into the database.

---

### 3. Loading Data into SQLite

After processing, the transformed data was loaded into a **SQLite** database, enabling efficient local queries through a lightweight `.db` file.

---

### 4. Building an AI Agent

With the data properly stored, I developed an **AI agent** capable of:

* Reading data from the SQLite database
* Interpreting user queries
* Providing answers based on the stored records

The agent acts as an intelligent layer over the database, allowing natural-language questioning.

---

### 5. Generating Charts and Visual Insights

Python scripts were implemented to:

* Query data directly from SQLite
* Generate visual charts based on the results
* Provide insights and answers in a graphical format

Libraries such as **Matplotlib** and **Pandas** were used for visualization.

---

## Technologies Used

* Python
* Pandas
* SQLite
* Matplotlib
* AI tools (ADK / chosen model)

---

## Project Goal

The goal of this project is to create a complete workflow demonstrating data engineering practices, data analysis, and applied artificial intelligence, all based on real-world public data and structured in a clean, educational, and robust way.
