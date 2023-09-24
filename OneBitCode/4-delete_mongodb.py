# 1 - Importar pymongo
from pymongo import MongoClient

# 2 - Estabelecer conexão com mongo DB
client = MongoClient()
print(client)

# 3 - Listar db
my_database = client.obcblog
my_collection = my_database.posts

# 4 - Deletar documento

my_query = {"category": "Backend"}

delete_my_query = my_collection.delete_one(my_query)

# 5 - Verificar exclusão
print(f"{delete_my_query.deleted_count} documento excluído.")