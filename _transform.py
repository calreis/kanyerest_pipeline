from datetime import datetime 
import extract
import requests
import sqlite3


# Transformação das Quotes(frases) em uma lista com frase e data de extração
def load_transform():
    frases = [] # lista vázia
    print(f'[{datetime.now()}] Iniciando transformações das frases.... ')
    data = f'{datetime.now()}' # module datetime com a data da extração
    frases.append(extract.extraction()['quote']) # modulo append para adicionar a frase
    frases.append(data) # adição da data 
    return frases # retorno da lista com frase e data


print(load_transform())
