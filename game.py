import utils, random, time, questionary, os
from rich.console import Console
from rich.table import Table

MAX_CHARACTERS = 3

# Lancer la partie
def start_game(pseudo_player):
    # Creation variable manche
    number_round_play = 0
    # Creer l'équipe
    team_of_characters = create_my_team()
    # Lancer la manche
    start_round(pseudo_player,team_of_characters, number_round_play)
    
def start_round(pseudo_player, team_of_characters,number_round_play):
    # Tant equipe vivant
    while is_team_alive(team_of_characters):
        # Incrémentation de 1 la variable manche
        number_round_play += 1
        # Creer l'enemi
        team_of_enemie = [create_enemie_team()]
        # Lancer l'attqaue de la manche
        start_round_attack(team_of_characters, team_of_enemie, number_round_play)
    # Enregistrer le résultat dans la bdd
    utils.save_result(pseudo_player, number_round_play)
        
# Creer l'équipe
def create_my_team():
    # Création de la liste équipe
    list_team_of_characters = []
    # Import de la liste de personnage
    list_characters_on_bdd = utils.list_characters_on_bdd("characters")
    # Tant que taille de l'équipe est pas pleine
    while len(list_team_of_characters) < MAX_CHARACTERS:
        # Demander un personnage
        character = ask_character(list_team_of_characters,list_characters_on_bdd)
        # Ajouter à l'équipe
        list_team_of_characters.append(character)
    # Retourne l'équipe
    return list_team_of_characters

def ask_character(list_team_of_characters,list_characters_on_bdd):
    # Afficher l'équipe
    create_list_of_option(create_list_text(list_team_of_characters))
    # Demander un personnage
    character = ask_valid_choice(create_list_text(list_characters_on_bdd))
    # Supp le personnage de la liste de choix
    return list_characters_on_bdd.pop(character-1)
    
# Liste de texte
def create_list_text(liste_character):
    # creation de liste de texte
    list_text = []
    # Pour personnage dans liste
    for person in liste_character:
        # Ajouter le texte à la liste
        list_text.append(f"{person["name"]} --- {person["ATK"]} ATK -- {person["DEF"]} DEF - {person["PV"]} PV")
    # Retourne liste text
    return list_text

# Afficher les options
def create_list_of_option(list_of_options):
    # Creation la liste des options
    option_list = []
    # Pour index, option in enumerees options
    for index, option in enumerate(list_of_options, start=1):
        # Ajouter à la liste index + option
        option_list.append(f"{index}- {option}")
    return option_list

# Demander un personnage
def ask_valid_choice(list_of_option):
    # Tant que vrai
    while True:
        # Demander un choix
        choice_ask =  ask_choice(list_of_option)
        # Si choix est valide parmi les options
        if is_choice_valid(choice_ask[0],1, len(list_of_option)):
            # Retourne le nombre
            return int(choice_ask[0])
        # Afficher message erreur
        print("Tu as fais une erreur recommence")
        
def ask_choice(list_of_option):
    return questionary.select(
            "Choisis une proposition :(1,2, ect) ",
            choices=create_list_of_option(list_of_option)
        ).ask()
        
# Choix valide parmis les options
def is_choice_valid(choice,minimum, maximum):
    # Si le choix n'est pas un nombre
    if not choice.isdigit():
        # Retourne Faux
        return False
    # Convertir en entier
    choice = int(choice)
    # Si l'entier n'est compris entre le min et max
    if  not is_between_min_max(minimum,choice,maximum):
        # Retourne Faux
        return False
    # Retourne Vrai
    return True

# Entier compris entre  minimum et maximum
def is_between_min_max(minimum,choice,maximum):
    return minimum <=  choice <= maximum

# équipe vivant ?
def is_team_alive(team):
    # Pour personnage dans equipe
    for person in team:
        # Si PV personnage supérieur à 0
        if person["PV"] > 0:
            # Retourne True
            return True
    # Retourne Faux
    return False

# Creation de l'ennemis
def create_enemie_team():
    # Liste personnage (ennemis)
    list_enemies_on_bdd = utils.list_characters_on_bdd("enemies")
    # Retourne l'ennemis au hasard
    return random.choice(list_enemies_on_bdd)

# Lancer la manche
def start_round_attack(team_of_characters, team_of_enemies, number_round_play):
    number_of_laps = 0
    # Tant que equipe vivant
    while is_team_alive(team_of_characters):
        # Incrémenter le nombre de round
        number_of_laps += 1
        # Attaque du Joueur 
        player_attack(team_of_characters, team_of_enemies,create_battle_data(number_round_play, number_of_laps, 1,team_of_characters, team_of_enemies))
        # Si pas equipe vivant (ennemis)
        if not is_team_alive(team_of_enemies):
            # break
            break
        # Attaque Ennemis
        player_attack(team_of_enemies,team_of_characters,create_battle_data(number_round_play, number_of_laps, 2,team_of_characters, team_of_enemies))

def create_battle_data(round_number, laps, turn, characters, enemies):
    return {
        "round": round_number,
        "laps": laps,
        "unOudeux": turn,
        "characterTeam": characters,
        "enemieTeam": enemies
    }


def player_attack(team_attack,team_deffense,dico_text ):
    # Attaque de l'equipe
    action_damage = team_player_attack(team_attack, team_deffense)
    # Ajouter les damages au text
    dico_text["damage"] = action_damage
    # Affichier de l'execution de team_player_attack
    show_array(dico_text)
    
#################################
########### Affichage ###########
#################################
    
def show_array(dico_text):
    side_text()
    console = Console()
    # Création du tableau
    array = create_array(dico_text)
    # Création du corp du tableau
    create_body_of_array(array, dico_text)
    console.print(array)

def side_text():
    time.sleep(0.8)
    os.system("cls")

def create_array(dico_text):
    return Table(
        title=f"[bold]MANCHE {dico_text['round']} --- Tour {dico_text['laps']} - {dico_text['unOudeux']}/2[/bold]",
        expand=True,
        padding=(1,1)
        
    )

def create_body_of_array(array, dico_text):
    # Création des colonnes
    create_column_of_array(array,["Allié", "Dégâts", "Ennemis"])
    # Création des ligne
    create_row_of_array(array,dico_text)
        
def create_column_of_array(array,columns):
    for column in columns:
        array.add_column(column, justify="center")
        
def create_row_of_array(array, dico_text):
    for index in range(MAX_CHARACTERS):
        # recupération du text
        text = recup_text(dico_text, index)
        # Ajouter les lignes
        array.add_row(f"[bold green]{text[0]}[/bold green]",text[1],f"[bold red]{text[2]}[/bold red]")
        
def recup_text(dico_text,index):
    # Récupérer le texte pour les allié
    text_allied = recup_character(dico_text["characterTeam"], index)
    # Récupérer le texte du combat
    text_damage = recup_element(dico_text["damage"], index)
    # Récupérer le texte pour les enemies
    text_ennemies = recup_character(dico_text["enemieTeam"],index)
    # Retourne les textes
    return text_allied,text_damage,text_ennemies

def recup_character(team,index):
    # Si assez de personne dans l'équipe
    if index >= len(team):
        # retourne text vide
        return ""
    # Récupération du personnage
    personnage = team[index]
    # Retourne le texte
    return f"{personnage['name']} - {personnage['PV']} PV"

def recup_element(damage, index):
    # Si assez de personne dans l'équipe
    if index >= len(damage):
        # retourne text vide
        return ""
    # Récupération de l'attaque
    damage = damage[index]
    # retourne le texte
    return f"{damage['character']} inflige {damage['damage']} dégâts à {damage['enemie']}"
    
def show_text_fight(liste):
    for texte in liste:
        print(texte)
    print("")

######################################
########## Mecanique du jeu ##########
######################################

# Attaque Joueur
def team_player_attack(team_attack, team_defense):
    # Liste action
    action_damage = []
    # Pour joueur dans l'équipe
    for person in team_attack:
        # Vérifier qu'il reste des ennemis vivants
        if not is_team_alive(team_defense):
            break
        # Faire l'attaque
        action = person_attack(person, team_defense)
        # Si action effectué
        if action is not None:
            # Attaque le joueur
            action_damage.append(action)
    return action_damage
        
# Attaque le joueur
def person_attack(person_attack, team_defense):
    # Si sup à 0
    if not sup_n(person_attack["PV"]):
        return None
    # Creation de la liste des personne vivant
    list_of_living_enemies = create_character_living(team_defense)
    # Choisir un joueur au hasard parmis ce qui sont en vis
    person_defense = random.choice(list_of_living_enemies)
    # Enlever dégat 
    action_attack = attack_person(person_attack, person_defense)        
    return action_attack

# sup à n
def sup_n(number):
    # retourne si n supérieur à 0
    return number > 0

def create_character_living(team_defense):
    # Creation de la liste des perso vivant
    list_alive_character = []
    # Pour enemie dans enemies
    for person_defense in team_defense:
        # Si vivant
        if person_defense["PV"] > 0:
            # Ajouter à la liste
            list_alive_character.append(person_defense)
    # retourne la liste
    return list_alive_character
    
# Enlever dégat
def attack_person(person_atatck, person_defense):
    # Compter les dégats
    damage = count_damage(person_atatck, person_defense)
    # Mettre les dégat
    take_damage(person_defense, damage)
    # Retourner le message
    return create_dic_damage(person_atatck, damage, person_defense)
    
def count_damage(person_attack, person_defense):
    # Calcul des dégats
    damage = person_attack["ATK"] - person_defense["DEF"]
    # Si pas inférieur à 0
    if damage <= 0:
        return 1
    return damage
    
def create_dic_damage(person_attack, damage, person_defense):
    return {"character": person_attack["name"],"damage": damage,"enemie": person_defense["name"]}

def take_damage(person_defense, damage):
    # Si sup à pv - deg
    if sup_n(person_defense["PV"] - damage):
        # pv =- deg
        person_defense["PV"] -= damage
    # Sinon
    else:
        # pv = 0
        person_defense["PV"] = 0

################################
########## Classement ##########
################################

# Voir le classement
def show_top_ranking():
    # Chercher la liste avec pseudo + résultat
    list_score_result_on_bdd = utils.recup_score_result()
    # Liste des meilleurs scores
    list_of_best_score = list_of_best(list_score_result_on_bdd, 10)
    # Afficher le classment
    show_classement(list_of_best_score)
    
def list_of_best(list_score_result_on_bdd, max_rank):
    # creation liste des meilleur score
    list_of_best_score = []
    # Pour index 10 fois
    for index in range(max_rank):
        # Chercher le plus au score dans la liste
        index_result = look_for_best_score_result(list_score_result_on_bdd)
        # Si pas de résultat
        if index_result == None:
            # Quitter la boucle
            break
        # Ajouter le meilleur score à la liste
        list_of_best_score.append({"name" : list_score_result_on_bdd[index_result]["name"], "score": list_score_result_on_bdd[index_result]["score"][0]})
        # Supp le meilleur score
        del list_score_result_on_bdd[index_result]["score"][0]
    return list_of_best_score
    
def show_classement(best_score):
    # recup le texte
    list_classement = create_list_of_option(f"{text["name"]} --> {text["score"]}" for text in best_score)
    # afficher le texte
    show_text_fight(list_classement)
    
def show_text_fight(list_classement):
    print("")
    print("CLASSEMENT")
    for text in list_classement:
        print(text)
    print("")
    
# Chercher le plus au score dans la liste
def look_for_best_score_result(list_score_result):
    # Creation du dic avec pseudo + score
    index_pseudo = None
    # Pour dic dans la liste
    for index, user in enumerate(list_score_result):   
        # Si aucun score
        if not user["score"]:
            continue  
        # Si le nombre est max
        if is_number_max(index_pseudo, user, list_score_result):
            # Remplacer le pseudo et le score
            index_pseudo =  index
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