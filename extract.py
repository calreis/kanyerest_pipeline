from datetime import datetime 
import requests
import sqlite3

# URL com o a API KENYE.REST
def extraction():
    '''print('=====================================')
    print('Extraindo Frase da Api Kanye.Rest ...')
    print('=====================================')'''
    url = f"https://api.kanye.rest/"
    response = requests.get(url)
    if response.status_code == 200: # status da requisição 
        return response.json() # Arquivo retorno em formato json
    else:
        raise Exception(f'Erro na API Kanye.Rest({response.status_code}) : {response.text}')

