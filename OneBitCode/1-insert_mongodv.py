# 1 - Instalar biblioteca externa pip install pymongo

# 2 - Importar pymongo
from pymongo import MongoClient

# 3 - Estabelecer conexão com mongo DB
client = MongoClient()
print(client)

# 4 - Criar database
my_database = client.obcblog
my_collection = my_database.posts


# 5 - Criar post
post1 = {
    "title": "FastAPI",
    "category": "Backend",
    "author": {
        "name": "Rodrigo",
        "email": "rodrigo@gmail.com"
    }
}

resulta = my_collection.insert_one(post1)
print("Documento incluído com sucesso!")


