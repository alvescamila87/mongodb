# 1 - Importar pymongo
from pymongo import MongoClient
from pprint import pprint

# 2 - Estabelecer conexão com mongo DB
client = MongoClient()
print(client)

# 3 - Listar db
my_database = client.obcblog
my_collection = my_database.posts

# 4 - Retorna UM documento
# result = my_collection.find_one()
# print(result)

# 5 - Retorna TODOS os documentos
result = my_collection.find()
# print(result)
for doc in result: 
    # print(f"{doc}")
    pprint(doc)