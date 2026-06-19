from datetime import datetime 
import extract
import _transform
import _load
import requests
import sqlite3

'''
conexão = _load.get_connection()
createtable = _load.create_table(conexão)
inserindo = _load.insertion(conexão)
consulta = _load.consult(conexão)
print(consulta)'''

# Pipeline simple com ETL 
print("==============================================================================================")
print("Pequeno projeto Kanye Rest para explicar como funciona o proesso de ETL na Engenharia de Dados")
print("==============================================================================================")
print("")


if __name__ == '__main__':
	# ABRIR CONEXÃO COM O DB
	conexão = _load.get_connection()

	# CRIAÇÃO OU PERMANÊNCIA DO BANDO DE DADOS
	createtable = _load.create_table(conexão)

	# INSERÇÃO DE DADOS 
	inserindo = _load.insertion(conexão)

	# FECHANDO A CONEXÃO COM O BANCO
	conexão.close()

print('==============================================================================================')
print('Os dados foram extraídos >> transformados >> e carregados no banco de dados ...')
print('')
print('==============================================================================================')
print('O trabalho foi finalizado!')
print('==============================================================================================')

