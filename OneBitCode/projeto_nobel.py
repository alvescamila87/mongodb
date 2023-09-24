# Projeto Prêmio Nobel com API

# 1- Lib para trilha de automação e fazer requisições de APIs
import requests
from pymongo import MongoClient

# 2 - Esabelece conexão com MongoDB e o Database
cliente = MongoClient()

db = cliente['nobel']

# 3 - Importar os Dados em Documentos
for collection_name in ['prizes', 'laureates']:
    # requisição na API
    response = requests.get(
        f"http://api.nobelprize.org/v1/{collection_name[:-1]}.json")

    # listar registros da API / inserir no banco de dados
    documents = response.json()[collection_name]    
    # print(documents)
    db[collection_name].insert_many(documents)

# 4 - Acessando coleções / Contagem de documentos na coleção
prizes = db['prizes']
laureates = db['laureates']

length_prizes = prizes.count_documents({})
length_laureates = laureates.count_documents({})

print(length_prizes)
print(length_laureates)