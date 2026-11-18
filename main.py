import utils, game, sys

# Afficher le menu
def menu():
    # Demander le pseudo
    pseudo = ask_pseudo()
    # tant que vrai
    while True:
        # Demander un choix valide
        choice = game.ask_valid_choice(["Lancer la partie","Voir le classement","Quitter"])
        # Rediriger en fonction du choix 
        redirection_choice(choice, pseudo)
        
# Demander le pseudo
def ask_pseudo():
    # Tant que vrai
    while True:
        # Demander un pseudo
        pseudo = input("Quel est ton pseudo : ")
        # Si le pseudo est utilisé
        if not is_pseudo_use(pseudo):
            # Ajouter pseudo à la bdd
            utils.add_pseudo_bdd(pseudo)
            # Retourne pseudo
            return pseudo
        # Affichage erreur
        print("Pseudo déjà utilisé")
              
# pseudo utilisé
def is_pseudo_use(pseudo):
    # Si pseudo est dans liste pseudo
    return pseudo in utils.list_users()

# Diriger en fonction du choix
def redirection_choice(choice, pseudo):
    # Si égal à 1
    if choice == 1:
        # Lancer la partie
        game.game_start(pseudo)
    # Elif égal à 2
    elif choice == 2:
        # Voir le classement
        game.show_ranking()
    # Sinon
    else:
        # Quitter le code
        sys.exit()
        
if __name__ == "__main__":
    menu()