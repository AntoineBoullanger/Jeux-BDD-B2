import utils, game, sys

# Afficher le menu
def menu():
    # Demander le pseudo
    pseudo_player = ask_pseudo_to_player()
    # tant que vrai
    while True:
        # Demander un choix valide
        choice_select_start = game.ask_valid_choice(["Lancer la partie","Voir le classement","Quitter"])
        # Rediriger en fonction du choix 
        redirection_choice(choice_select_start, pseudo_player)
        
# Demander le pseudo
def ask_pseudo_to_player():
    # Tant que vrai
    while True:
        # Demander un pseudo
        pseudo_player = input("Quel est ton pseudo : ")
        # Si le pseudo respect les conditions
        if is_pseudo_respect_condition(pseudo_player):
            # Retourne pseudo
            return pseudo_player
        # Affichage erreur
        print("Pseudo doit être entre 3 et 10 caractères")
              
# pseudo utilisé
def is_pseudo_respect_condition(pseudo_player):
    # Si pseudo respect la longueur
    if not game.is_between_min_max(3,len(pseudo_player),10):
            # retourne faux
            return False
    # si pseudo utilisé
    if not pseudo_player in utils.list_users():
        print("Bienvenue sur le jeu")
        # ajouter le pseudo
        utils.add_pseudo_bdd(pseudo_player)
    return True
    

# Diriger en fonction du choix
def redirection_choice(choice, pseudo):
    # Si égal à 1
    if choice == 1:
        # Lancer la partie
        game.start_game(pseudo)
    # Elif égal à 2
    elif choice == 2:
        # Voir le classement
        game.show_top_ranking()
    # Sinon
    else:
        # Quitter le code
        sys.exit()
        
if __name__ == "__main__":
    menu()