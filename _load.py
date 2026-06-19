from datetime import datetime 
import _transform
import extract
import requests
import sqlite3

# 1. FUNÇÃO PARA CRIAÇÃO E CONEXÃO DO BANCO DE DADOS
def get_connection():
    return sqlite3.connect("kanyewest.db")

# 2. FUNÇÃO PARA CRIAÇÃO DA TABELA (Chamada uma única vez)
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS frases_kanye(frase TEXT, data TEXT)")
    conn.commit()

# 3. FUNÇÃO PARA INSERÇÃO DE DADOS (Usa Placeholders e Commit)
def insertion(conn):
    cursor = conn.cursor()
    dados = _transform.load_transform() # Assume que retorna (frase, data)
    
    # Usa '?' para evitar erros de sintaxe e injeção de SQL
    cursor.execute("INSERT INTO frases_kanye(frase, data) VALUES (?, ?)", (dados[0], dados[1]))
    conn.commit() # Salva as alterações no banco

# 4. FUNÇÃO PARA CONSULTA
def consult(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM frases_kanye') 
    return cursor.fetchall()

