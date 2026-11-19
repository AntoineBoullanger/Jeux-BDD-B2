import utils, random, time, questionary, os
from rich.console import Console
from rich.table import Table

MAX_CHARACTERS = 3

# Lancer la partie
def game_start(pseudo):
    # Creation variable manche
    n_round = 0
    # Creer l'équipe
    team = create_team()
    # Tant equipe vivant
    while is_team_alive(team):
        # Incrémentation de 1 la variable manche
        n_round += 1
        # Creer l'enemi
        enemie = [create_enemie()]
        # Lancer la manche
        start_round(team, enemie, n_round)
    # Enregistrer le résultat dans la bdd
    # utils.save_result(pseudo, round)
    


# Creer l'équipe
def create_team():
    # Création de la liste équipe
    list_team = []
    # Import de la liste de personnage
    list_characters = utils.list_characters("characters")
    # Tant que taille de l'équipe est pas pleine
    while len(list_team) < MAX_CHARACTERS:
        # Afficher l'équipe
        show_options(create_list_text(list_team))
        # Demander un personnage
        character = ask_valid_choice(create_list_text(list_characters))
        # Ajouter le personnage à l'equipe
        list_team.append(list_characters[character-1])
        # Supp le personnage de la liste de choix
        del list_characters[character-1]
    # Retourne l'équipe
    return list_team

# Liste de texte
def create_list_text(liste_character):
    # creation de liste de texte
    list_text = []
    # Pour personnage dans liste
    for character in liste_character:
        # Ajouter le texte à la liste
        list_text.append(f"{character["name"]} --- {character["ATK"]} ATK -- {character["DEF"]} DEF - {character["PV"]} PV")
    # Retourne liste text
    return list_text

# Afficher les options
def show_options(options):
    # Creation la liste des options
    option_list = []
    # Pour index, option in enumerees options
    for index, option in enumerate(options, start=1):
        # Ajouter à la liste index + option
        option_list.append(f"{index}- {option}")
    return option_list

# Demander un personnage
def ask_valid_choice(list_of_option):
    # Tant que vrai
    while True:
        # Demander un choix
        choice =  ask_choice(list_of_option)
        # Si choix est valide parmi les options
        if is_choice_valid(choice[0], len(list_of_option)):
            # Retourne le nombre
            return int(choice[0])
        # Afficher message erreur
        print("Tu as fais une erreur recommence")
        
def ask_choice(list_of_option):
    return questionary.select(
            "Choisis une proposition :(1,2, ect) ",
            choices=show_options(list_of_option)
        ).ask()
        
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
def is_team_alive(team):
    # Pour personnage dans equipe
    for character in team:
        # Si PV personnage supérieur à 0
        if character["PV"] > 0:
            # Retourne True
            return True
    # Retourne Faux
    return False

# Lancer la manche
def start_round(team, enemies, n_round):
    laps= 0
    # Tant que equipe vivant
    while is_team_alive(team):
        # Incrémenter le nombre de round
        laps += 1
        # Attaque du Joueur 
        player_attack(team, enemies,n_round, laps, 1, team, enemies)
        # Si pas equipe vivant (ennemis)
        if not is_team_alive(enemies):
            # break
            break
        # Attaque Ennemis
        player_attack(enemies, team,n_round, laps, 2, team, enemies)
        
def player_attack(team,enemies,n_round,laps, n, team_show, enemies_show):
    # Attaque de l'equipe
    action_damage = team_player_attack(team, enemies)
    # Affichier de l'execution de team_player_attack
    time.sleep(1)
    os.system("cls")
    show_array(action_damage,team_show, enemies_show,n_round,laps,n)
    
def show_array(action_damage, team, enemies,n_round, laps, n):
    console = Console()
    # Creation du tableau
    table = Table(title=f"MANCHE {n_round} --- Tour {laps} - {n}/2",)
    # Ajouter les colonne
    add_column(table,["Allié","Dégât","Enemis"])
    # Pour le nombre max de personnage
    for i in range(MAX_CHARACTERS):
        # Récupérer le texte pour les allié
        element_allie = f"{team[i]["name"]} - {team[i]["PV"]} PV"
        # Récupérer le texte du combat
        element_damage = recup_element(action_damage, i)
        # Récupérer le texte pour les enemies
        element_ennemies = recup_element_a(enemies,i)
        # Ajouter la ligne
        table.add_row(element_allie,element_damage,element_ennemies)
    console.print(table)

def add_column(table, liste):
    # Pour chaque colonne dans la liste
    for column in liste:
        # Ajouter la colonne
        table.add_column(column)

def recup_element(action_damage, i):
    # Si assez d'élément dans action_damage
    if i < len(action_damage):
        # return l'action
        return f"{action_damage[i]["allie"]} attaque {action_damage[i]["enemy"]} --- {action_damage[i]["damage"]} dégats"
    # return text vide
    return ""
    
def recup_element_a(enemies, i):
    # Si assez d'élément dans action_damage
    if i < len(enemies):
        # return l'action
        return f"{enemies[i]["name"]} - {enemies[i]["PV"]} PV"
    # return text vide
    return ""
    
def show_text_fight(liste):
    for texte in liste:
        print(texte)
    print("")

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
        if not is_team_alive(enemies):
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
    living_enemies = create_character_living(enemies)
    # Choisir un joueur au hasard parmis ce qui sont en vis
    enemie = random.choice(living_enemies)
    # Enlever dégat 
    action_attack = attack(character, enemie)        
    return action_attack
    
def choose_enemie_random(living_enemies):
    # Si tous les personnages morts
    if living_enemies == []:
        return None
    # Retourne un joueur au hasard
    return random.choice(living_enemies)

def create_character_living(enemies):
    # Creation de la liste des perso vivant
    list_alive_character = []
    # Pour enemie dans enemies
    for enemie in enemies:
        # Si vivant
        if enemie["PV"] > 0:
            # Ajouter à la liste
            list_alive_character.append(enemie)
    # retourne la liste
    return list_alive_character
            
# sup à n
def sup_n(n):
    # retourne si n supérieur à 0
    return n > 0
    
# Enlever dégat
def attack(character, enemie):
    # Compter les dégats
    damage = count_damage(character, enemie)
    # Mettre les dégat
    take_damage(enemie, damage)
    # Retourner le message
    return show_damage(character, damage, enemie)
    
def count_damage(character, enemie):
    # Calcul des dégats
    damage = character["ATK"] - enemie["DEF"]
    # Si pas inférieur à 0
    if damage <= 0:
        return 1
    return damage
    
def show_damage(character, damage, enemie):
    return {"allie": character["name"],"damage": damage,"enemy": enemie["name"]}

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
    # Liste des meilleurs scores
    best_score = list_of_best(list_score_result, 10)
    # Afficher le classment
    show_classement(best_score)
    
def list_of_best(list_score_result, max_rank):
    # creation liste des meilleur score
    best_score = []
    # Pour index 10 fois
    for i in range(max_rank):
        # Chercher le plus au score dans la liste
        index_result = look_for_best_score_result(list_score_result)
        # Si pas de résultat
        if index_result == None:
            # Quitter la boucle
            break
        # Ajouter le meilleur score à la liste
        best_score.append({"name" : list_score_result[index_result]["name"], "score": list_score_result[index_result]["score"][0]})
        # Supp le meilleur score
        del list_score_result[index_result]["score"][0]
    return best_score
    
def show_classement(best_score):
    # recup le texte
    list_classement = show_options(f"{text["name"]} --> {text["score"]}" for text in best_score)
    # afficher le texte
    show_text_fight(list_classement)
    
# Chercher le plus au score dans la liste
def look_for_best_score_result(list_score_result):
    # Creation du dic avec pseudo + score
    index_pseudo = None
    # Pour dic dans la liste
    for i, user in enumerate(list_score_result):   
        # Si aucun score
        if not user["score"]:
            continue  
        # Si le nombre est max
        if is_number_max(index_pseudo, user, list_score_result):
            # Remplacer le pseudo et le score
            index_pseudo =  i
    # Retourner l'index du meilleur score
    return index_pseudo

def is_number_max(index_pseudo, user, list_score_result):
    # Si pas de score max
    if index_pseudo is None:
        # return False
        return True
    # Si score est supérieur à l'actuel
    if user["score"][0] > list_score_result[index_pseudo]["score"][0]:
        # retourne Faux
        return True
    return False
    
game_start("azef")