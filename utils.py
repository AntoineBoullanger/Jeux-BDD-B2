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
def list_characters_on_bdd(name_of_table):
    # Retourne liste des personnage
    return list(db[name_of_table].find({}, { "_id": 0}))

  
# Enregistrer le résultat dans la bdd
def save_result(pseudo, result):
    # Aller chercher la liste de résultat
    list_score = db["users"].find_one({"name" : pseudo},{"_id" : 0,"score" : 1})["score"]
    # Ajouter le résulter à la liste
    list_score.append(result)
    # Trier la liste dans l'ordre décorissant
    list_score_max_to_min = sorted(list_score, reverse=True)
    # Mettre sur la bdd
    db["users"].update_one({"name": pseudo}, {"$set": {"score": list_score_max_to_min}})
    
# Chercher la liste avec pseudo + résultat
def recup_score_result():
    # Retourne liste de pseudo + résultat
    return list(db["users"].find({},{"_id" : 0}))
    
    
