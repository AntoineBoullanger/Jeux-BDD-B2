import utils, random, time

MAX_CHARACTERS = 3

# Lancer la partie
def game_start(pseudo):
    # Creation variable manche
    round = 0
    # Creer l'équipe
    team = create_team()
    # Tant equipe vivant
    while team_alive(team):
        # Incrémentation de 1 la variable manche
        round += 1
        # Affichage Manche
        print("")
        print("-"*30)
        print(f"Manche - {round}")
        print("-"*30)
        # Lancer la manche
        start_round(team)
    # Afficher le résultat
    print(f"Résultat : Manche - {round} ")
    # Enregistrer le résultat dans la bdd
    utils.save_result(pseudo, round)
    


# Creer l'équipe
def create_team():
    # Création de la liste équipe
    list_team = []
    # Import de la liste de personnage
    list_characters = utils.list_characters("characters")
    # Tant que taille de l'équipe est pas pleine
    while len(list_team) < MAX_CHARACTERS:
        # Afficher l'équipe
        print("")
        print("Ma Team : ")
        show_team(list_team)
        print("")
        # Demander un personnage
        character = ask_character(list_characters)
        # Ajouter le personnage à l'equipe
        list_team.append(list_characters[character-1])
        # Supp le personnage de la liste de choix
        del list_characters[character-1]
    # Retourne l'équipe
    return list_team

# Afficher l'équipe
def show_team(list_team):
    # Pour index, personnage dans enumerate l'équipe
    for index, character in enumerate(list_team):
        # Afficher index + personnage
        print(f"{index+1}- {character["name"]} --- {character["ATK"]} ATK - {character["DEF"]} DEF - {character["PV"]} PV ")

# Demander un personnage
def ask_character(list_characters):
    # Tant que vrai
    while True:
        # Afficher les options
        print("Personnage à choisir")
        show_team(list_characters)
        # Demander un choix
        choice = input("Choisit un personnage : (1,2,3, ect) ")
        # Si choix est valide parmi les options
        if is_choice_valid(choice, len(list_characters)):
            # Retourne le nombre
            return int(choice)
        # Afficher message erreur
        print("Tu as fais une erreur recommence")
        
# Choix valide parmis les options
def is_choice_valid(choice, maximum):
    # Si le choix n'est pas un nombre
    if not choice.isdigit():
        # Retourne Faux
        return False
    # Convertir en entier
    choice = int(choice)
    # Si l'entier n'est compris entre le min et max
    if  not(1 <=  choice <= maximum):
        print("a")
        # Retourne Faux
        return False
    # Retourne Vrai
    return True
            
# équipe vivant ?
def team_alive(team):
    # Pour personnage dans equipe
    for character in team:
        # Si PV personnage supérieur à 0
        if character["PV"] > 0:
            # Retourne True
            return True
    # Retourne Faux
    return False

# Lancer la manche
def start_round(team):
    small_round = 0
    # Creation de l'ennemis
    enemie = [create_enemie()]
    # Tant que equipe vivant
    while team_alive(team):
        # Incrémenter le nombre de round
        small_round += 1
        # Afficher le nombre de round
        print(f"{10*"#"} ROUND {small_round} {10*"#"}")
        time.sleep(1)
        # Attaque du Joueur team
        team_player_attack(team, enemie)
        print("")
        # Si pas equipe vivant (ennemis)
        if not team_alive(enemie):
            # break
            break
        time.sleep(1)
        # Attaque Ennemis
        team_enemies_attack(team,enemie)
        print("")

# Creation de l'ennemis
def create_enemie():
    # Liste personnage (ennemis)
    list_enemies = utils.list_characters("enemies")
    # Retourne l'ennemis au hasard
    return random.choice(list_enemies)

    
# Attaque Joueur
def team_player_attack(team, enemie):
    # Afficher les joueur
    print("")
    print("YOUR TEAM")
    show_team(team)
    print("")
    # Pour joueur dans l'équipe
    for character in team:
        # Attaque le joueur
        character_attack(character,enemie)
        
# Attaque le joueur
def character_attack(character, enemie):
    # Si sup à 0
    if sup_n(character["PV"]):
        # Enlever dégat 
        attack(character, enemie[0])
        
        
# sup à n
def sup_n(n):
    # Si pv supérieur à 0
    if n > 0:
        # retourne True
        return True
    # Retourne False
    return False
    
# Enlever dégat
def attack(character, enemie):
    # Compter les dégats
    damage = character["ATK"] - enemie["DEF"]
    # Si pas inférieur à 0
    if damage <= 0:
        damage = 0
    take_damage(enemie, damage)
    # Afficher les dégats
    print(f"{character["name"]} inflige {damage} dégats à {character["name"]}")


def take_damage(enemie, damage):
    # Si sup à pv - deg
    if sup_n(enemie["PV"] - damage):
        # pv =- deg
        enemie["PV"] -= damage
    # Sinon
    else:
        # pv = 0
        enemie["PV"] = 0

    

# Attaque Ennemis
def team_enemies_attack(team,enemie):
    # Afficher l'ennemis
    print("")
    print("ENEMIES")
    show_team(enemie)
    print("")
    # Choisir un joueur au hasard parmis ce qui sont en vis
    character = random.choice([character for character in team if character["PV"] >0])
    # Compter les dégats
    attack(enemie[0], character)
    
# Voir le classement
    # Chercher la liste avec pseudo + résultat
    pseudo_and_result = "a"
    # Pour index 10 fois
        # Chercher le plus au score dans la liste
        # Afficher le plus au score index+1 + pseudo + score
    
# Chercher le plus au score dans la liste
    # Creation du dic avec pseudo + score
    # Pour dic dans la liste
        # Trouver le max de la liste du dic
        # Si max de la liste supérieur à score
            # Remplacer le pseudo et le score
        
game_start("Antoine")