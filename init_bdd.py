from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["base"]
characters = db["characters"]
enemies = db["enemies"]
users = db["users"]

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
    "ATK": [18, 22, 20, 16, 19, 17, 21, 23, 20, 24],
    "DEF": [17, 19, 18, 22, 19, 16, 17, 15, 20, 21],
    "PV": [120, 140, 125, 150, 120, 110, 115, 125, 135, 145]
}

list_enemies = {
    "name": [
        "Empire romain",
        "Angleterre",
        "Saint-Empire romain germanique",
        "Allemagne",
        "Prusse",
        "Autriche",
        "Espagne",
        "Russie",
        "Empire ottoman",
        "Bourgogne"
    ],
    "ATK": [10, 13, 15, 17, 18, 20, 22, 23, 25, 27],
    "DEF": [5, 7, 10, 11, 12, 14, 15, 16, 18, 20],
    "PV": [55, 70, 85, 95, 105, 115, 125, 135, 145, 160]
}

for i in range(len(list_characters["name"])):
    characters.insert_one({"name" : list_characters["name"][i], "ATK": list_characters["ATK"][i], "DEF" : list_characters["DEF"][i], "PV": list_characters["PV"][i]})
    enemies.insert_one({"name" : list_enemies["name"][i], "ATK": list_enemies["ATK"][i], "DEF" : list_enemies["DEF"][i], "PV": list_enemies["PV"][i]})

    
    
    
    
