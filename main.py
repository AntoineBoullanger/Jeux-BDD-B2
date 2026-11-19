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
        # Si le pseudo est utilisé
        if not is_pseudo_already_use(pseudo_player):
            # Ajouter pseudo à la bdd
            utils.add_pseudo_bdd(pseudo_player)
            # Retourne pseudo
            return pseudo_player
        # Affichage erreur
        print("Pseudo déjà utilisé")
              
# pseudo utilisé
def is_pseudo_already_use(pseudo_player):
    # Si pseudo est dans liste pseudo
    return pseudo_player in utils.list_users()

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