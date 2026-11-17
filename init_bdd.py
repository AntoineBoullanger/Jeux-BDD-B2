from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["base"]
characters = db["characters"]
enemies = db["enemies"]
users = db["users"]

list_users = {
    "name" : 
        "Antoine"
    ,"score" : 
        [3,5,8]
}

list_characters = {
    "name": [
        "Clovis Ier",
        "Charlemagne",
        "Philippe Auguste",
        "Saint Louis",
        "Philippe IV le Bel",
        "Charles VII",
        "Louis XI",
        "François Ier",
        "Henri IV",
        "Louis XIV"
    ],
    "ATK": [18, 22, 20, 17, 19, 16, 21, 23, 20, 25],
    "DEF": [15, 18, 16, 20, 17, 14, 15, 13, 18, 19],
    "PV": [120, 130, 115, 140, 110, 105, 110, 120, 130, 150]
}

list_enemies = {
    "name": [
        "Empire romain",
        "Angleterre",
        "Espagne",
        "Saint-Empire romain germanique",
        "Autriche",
        "Prusse",
        "Bourgogne",
        "Empire ottoman",
        "Russie",
        "Allemagne"
    ],
    "ATK": [10, 20, 35, 12, 25, 18, 30, 22, 28, 15],
    "DEF": [5, 8, 20, 6, 15, 10, 25, 12, 18, 7],
    "PV": [50, 120, 300, 70, 200, 100, 250, 150, 180, 90]
}

users.insert_one(list_users)

for i in range(len(list_characters["name"])):
    characters.insert_one({"name" : list_characters["name"][i], "ATK": list_characters["ATK"][i], "DEF" : list_characters["DEF"][i], "PV": list_characters["PV"][i]})
    enemies.insert_one({"name" : list_enemies["name"][i], "ATK": list_enemies["ATK"][i], "DEF" : list_enemies["DEF"][i], "PV": list_enemies["PV"][i]})

    
    
    
    
