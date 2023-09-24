# 1 - Importar pymongo
from pymongo import MongoClient

# 2 - Estabelecer conexão com mongo DB
client = MongoClient()
print(client)

# 3 - Listar db
my_database = client.obcblog
my_collection = my_database.posts

# 4 - Atualizar documentos

old_value = {"title": "Python com Mongo DB",
             "category": "Banco de dados"             
             }

new_value = {"$set":{
            "title": "Streamlit",
             "category": "Data Analysis"
             }}

my_collection.update_one(old_value, new_value)

# 5 - Verificar se deu certo a atualização 
for doc in my_collection.find():
    print(doc)