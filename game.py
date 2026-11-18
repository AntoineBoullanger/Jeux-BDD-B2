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
        show_round(round)
        # Creer l'enemi
        enemie = [create_enemie()]
        # Lancer la manche
        start_round(team, enemie)
    # Afficher le résultat
    print(f"Résultat : Manche - {round} ")
    # Enregistrer le résultat dans la bdd
    # utils.save_result(pseudo, round)
    
def show_round(round):
    print("")
    print("-"*30)
    print(f"Manche - {round}")
    print("-"*30)

# Creer l'équipe
def create_team():
    # Création de la liste équipe
    list_team = []
    # Import de la liste de personnage
    list_characters = utils.list_characters("characters")
    # Tant que taille de l'équipe est pas pleine
    while len(list_team) < MAX_CHARACTERS:
        # Afficher l'équipe
        show_options([f"{character["name"]} --- {character["ATK"]} - {character["DEF"]} - {character["PV"]} PV" for character in list_team])
        # Demander un personnage
        character = ask_valid_choice(list_characters)
        # Ajouter le personnage à l'equipe
        list_team.append(list_characters[character-1])
        # Supp le personnage de la liste de choix
        del list_characters[character-1]
    # Retourne l'équipe
    return list_team    

# Afficher les options
def show_options(options):
    print("")
    # Pour index, option in enumerees options
    for index, option in enumerate(options, start=1):
        # Afficher index + option
        print(f"{index}- {option}")

# Demander un personnage
def ask_valid_choice(list_of_option):
    # Tant que vrai
    while True:
        # Afficher les options
        show_options([f"{character["name"]} --- {character["ATK"]} - {character["DEF"]} - {character["PV"]} PV" for character in list_of_option])
        # Demander un choix
        choice = input("Qu'est ce que tu veux faire ? (1,2 ou 3) ")
        # Si choix est valide parmi les options
        if is_choice_valid(choice, len(list_of_option)):
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
def start_round(team, enemies):
    laps= 0
    # Tant que equipe vivant
    while team_alive(team):
        # Incrémenter le nombre de round
        laps += 1
        # Attaque du Joueur team
        action_damage = team_player_attack(team, enemies)
        # Affichier le texte
        show_text(action_damage,team,laps,1)
        # Si pas equipe vivant (ennemis)
        if not team_alive(enemies):
            # break
            break
        # Attaque Ennemis
        action_damage = team_player_attack(enemies,team)
        show_text(action_damage,enemies,laps,2)
        
def show_text(action_damage, team,laps, n):
    # Afficher le round
    show_laps(laps, n)
    # Afficher l'équipe
    show_options([f"{character["name"]} --- {character["PV"]} PV" for character in team])
    # Afficher les dégats
    show_options(action_damage)

def show_laps(laps,n):
    print(f"{10*"#"} TOUR {laps} - {n}/2 {10*"#"}")
    time.sleep(1)

# Creation de l'ennemis
def create_enemie():
    # Liste personnage (ennemis)
    list_enemies = utils.list_characters("enemies")
    # Retourne l'ennemis au hasard
    return random.choice(list_enemies)

# Attaque Joueur
def team_player_attack(team, enemies):
    # Liste action
    action_damage = []
    # Pour joueur dans l'équipe
    for character in team:
            # Vérifier qu'il reste des ennemis vivants
        if not team_alive(enemies):
            break
        # Faire l'attaque
        action = character_attack(character, enemies)
        # Si action effectué
        if action is not None:
            # Attaque le joueur
            action_damage.append(action)
    return action_damage
        
# Attaque le joueur
def character_attack(character, enemies):
    # Si sup à 0
    if not sup_n(character["PV"]):
        return None
    # Creation de la liste des personne vivant
    living_enemies = [enemy for enemy in enemies if enemy["PV"] > 0]
    # Si plus d'enemi
    if not living_enemies:
        return None
    # Choisir un joueur au hasard parmis ce qui sont en vis
    enemie = random.choice(living_enemies)
    # Enlever dégat 
    action_attack = attack(character, enemie)        
    return action_attack
            
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
    # Retourner le message
    return show_damage(character, damage, enemie)
    
def show_damage(character, damage, enemie):
    return f"{character["name"]} inflige {damage} dégats à {enemie["name"] }"

def take_damage(enemie, damage):
    # Si sup à pv - deg
    if sup_n(enemie["PV"] - damage):
        # pv =- deg
        enemie["PV"] -= damage
    # Sinon
    else:
        # pv = 0
        enemie["PV"] = 0

# Voir le classement
def show_ranking():
    # Chercher la liste avec pseudo + résultat
    list_score_result = utils.recup_score_result()
    # Pour index 10 fois
    for i in range(10):
        # Chercher le plus au score dans la liste
        index_result = look_for_best_score_result(list_score_result)
        # Afficher le plus au score index+1 + pseudo + score
        show_max_score(list_score_result, index_result, i)
        # Supp le meilleur score
        del list_score_result[index_result]["score"][0]
        
def show_max_score(list_score_result, index_result,i):
    print(f"{i+1}- {list_score_result[index_result]["name"]} --- {list_score_result[index_result]["score"][0]} ")
    
# Chercher le plus au score dans la liste
def look_for_best_score_result(list_score_result):
    # Creation du dic avec pseudo + score
    index_pseudo = 0
    # Pour dic dans la liste
    for i in range(1,len(list_score_result)):   
        # Si liste vide passer
        if list_score_result[i]["score"] == []:
            continue  
        # Si max de la liste supérieur à score
        if list_score_result[i]["score"][0] > list_score_result[index_pseudo]["score"][0] :
            # Remplacer le pseudo et le score
            index_pseudo =  i
    return index_pseudo
        
