from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["base"]

# Liste des pseudos
def list_users():
    # Retourne la liste des pseudos
    return [doc["name"] for doc in db["users"].find({}, {"name": 1, "_id": 0})]

# Ajouter pseudo à la bdd
def add_pseudo_bdd(pseudo):
    # Ajouter à la bdd
    db["users"].insert_one({"name" : pseudo, "score" : []})
    
# Liste des personnage
    # Retourne liste des personnage
    

    
# Enregistrer le résultat dans la bdd
    # Aller chercher la liste de résultat
    # Ajouter le résulter à la liste
    # Mettre sur la bdd
    
# Chercher la liste avec pseudo + résultat
    # Retourne liste de pseudo + résultat