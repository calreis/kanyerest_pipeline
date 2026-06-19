# 🎧 Kanye Rest ETL Pipeline

[![Python](https://shields.io)](https://python.org)
[![Docker](https://shields.io)](https://docker.com)
[![SQLite](https://shields.io)](https://sqlite.org)

Uma pipeline de dados (ETL) modular e conteinerizada desenvolvida para demonstrar os fundamentos da Engenharia de Dados. O projeto consome frases aleatórias do artista Kanye West, aplica transformações estruturais com marcação temporal e persiste os dados em um banco de dados local.

## 🚀 Arquitetura do Projeto

O projeto segue os princípios de desacoplamento de responsabilidades, dividindo o ciclo de vida dos dados em módulos independentes:

*   **Extract (`extract.py`):** Consome a API REST `https://kanye.rest` tratando códigos de status HTTP.
*   **Transform (`_transform.py`):** Captura a carga bruta (JSON), gera um carimbo de data/hora estruturado (`datetime`) e organiza as informações em uma estrutura de lista ideal para carga.
*   **Load (`_load.py`):** Gerencia a conexão idempotente com o **SQLite**, criando tabelas de forma segura (`IF NOT EXISTS`) e realizando inserções parametrizadas protegidas contra SQL Injection.
*   **Main (`main.py`):** O orquestrador central do fluxo que gerencia o ciclo de vida da conexão do banco utilizando tratamento de exceções robusto (`try/finally`).

## 🛠️ Tecnologias e Boas Práticas

*   **Python 3.11-slim:** Imagem base reduzida para otimização de recursos de CPU/memória no deploy.
*   **Docker:** Conteinerização total da aplicação.
*   **Volumes Docker (`-v`):** Utilizados para garantir a persistência física do arquivo `.db` fora do container.
*   **Automação via Cron:** Agendamento configurado para orquestração diária automatizada.
*   **Análise de Dados com Pandas:** Script complementar focado em carregar e analisar a evolução das ingestões.

## 📦 Como Executar

### Pré-requisitos
* Docker instalado.

### 1. Construir a Imagem Docker
```bash
docker build -t pipeline-kanye .
```

### 2. Executar em Segundo Plano (Modo Detached com Persistência)
Para rodar a pipeline garantindo que o banco de dados seja salvo no seu host real (ex: pasta local ou servidor DietPi):
```bash
docker run -d --rm -v /seu/caminho/absoluto:/app pipeline-kanye
```

### 3. Orquestração com Cron (Execução Diária à Meia-Noite)
Adicione a seguinte linha ao seu `crontab -e` para automatizar o processo e coletar logs:
```text
0 0 * * * docker run --rm -v /seu/caminho/absoluto:/app pipeline-kanye >> /seu/caminho/absoluto/pipeline.log 2>&1
```

## 📊 Visualização dos Dados (Pandas)
Para consultar a base de dados ingerida de forma analítica, utilize o script de visualização:
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("kanyewest.db")
df = pd.read_sql_query("SELECT * FROM frases_kanye ORDER BY data DESC", conn)
print(df.head())
conn.close()
```
<<<<<<< HEAD
=======

>>>>>>> d3c1d93 (chore: configurar ambiente virtual e corrigir nome do README)
