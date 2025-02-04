from pymongo import MongoClient, ASCENDING
import json

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.mycollection

# Insérer des documents initiaux
documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]

result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)

# Recherche d'un utilisateur qui n'existe pas
query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

# Recherche des utilisateurs ayant un âge > 25
query = {"age": {"$gt": 25}}
documents = collection.find(query)

for doc in documents:
    print(doc)

# Mise à jour : Incrémenter l'âge de ceux qui ont un âge > 25
update = {"$inc": {"age": 1}}
result = collection.update_many(query, update)
print("Modified document count:", result.modified_count)

# Suppression des utilisateurs avec un âge > 25
result = collection.delete_many(query)
print("Deleted document count:", result.deleted_count)

# Recherche avec condition multiple (âge > 25 et email finissant par @example.com)
query = {
    "$and": [
        {"age": {"$gt": 25}},
        {"email": {"$regex": "@example\\.com$"}}
    ]
}
documents = collection.find(query)

for doc in documents:
    print(doc)

# Projection (récupérer seulement name et email, sans _id)
projection = {"_id": 0, "name": 1, "email": 1}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)

# Trier les résultats par nom
documents = collection.find(query).sort("name", ASCENDING)

for doc in documents:
    print(doc)

# 📥 Charger des données depuis un fichier JSON
try:
    with open("accounts.json", "r") as file:
        data = json.load(file)  # Lire en tant que liste d'objets
    result = collection.insert_many(data)
    print("Inserted data with the following IDs:", result.inserted_ids)
except json.JSONDecodeError as e:
    print("Erreur JSON:", e)
except FileNotFoundError:
    print("Le fichier accounts.json n'existe pas.")

# 🔍 Supprimer les doublons avant de créer l'index unique
pipeline = [
    {"$group": {"_id": "$email", "doc": {"$first": "$$ROOT"}}},
    {"$replaceRoot": {"newRoot": "$doc"}}
]

deduplicated_docs = list(collection.aggregate(pipeline))
collection.delete_many({})  # Supprime tout
collection.insert_many(deduplicated_docs)  # Réinsère les documents uniques

# 📌 Création d’un index unique sur le champ email
index_name = collection.create_index("email", unique=True)
print(f"Index unique créé : {index_name}")

# Recherche d'utilisateurs d'une ville spécifique avec un index
index_name = collection.create_index("address.city", name="city_index")

city = "Bradshawborough"
results = collection.find({"address.city": city})

for result in results:
    print(result)

# Recherche de comptes avec un solde supérieur à 30 000
min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})

for result in results:
    print(result)

# 🔄 Agrégation : Total des soldes par ville
pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(f"{result['_id']}: {result['total_balance']}")

# 🔢 Compter les utilisateurs par tranche d’âge
pipeline = [
    {"$match": {"age": {"$gt": 25}}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(result)
