import utils, game, sys

# Afficher le menu
def menu():
    # Demander le pseudo
    pseudo = ask_pseudo()
    # tant que vrai
    while True:
        # Demander un choix valide
        choice = ask_valid_choice()
        # Rediriger en fonction du choix 
        redirection_choice(choice, pseudo)
        
# Demander le pseudo
def ask_pseudo():
    # Tant que vrai
    while True:
        # Demander un pseudo
        pseudo = input("Quel est ton pseudo : ")
        # Si le pseudo est utilisé
        if pseudo_use(pseudo):
            # Ajouter pseudo à la bdd
            utils.add_pseudo_bdd(pseudo)
            # Retourne pseudo
            return pseudo
        # Affichage erreur
        print("Pseudo déjà utilisé")
            
        
# pseudo utilisé
def pseudo_use(pseudo):
    # Si pseudo est dans liste pseudo
    if pseudo in utils.list_users():
        # Retourne Faux
        return False
    # Retourne True
    return True

# Demander un choix valide
def ask_valid_choice():
    # Tant que vrai
    while True:
        # Creation des option
        options = ["Lancer la partie","Voir le classement","Quitter"]
        # Afficher les options
        show_options(options)
        # Demander un choix
        choice = input("Qu'est ce que tu veux faire ? (1,2 ou 3)")
        # Si choix est valide parmi les options
        if game.is_choice_valid(choice, len(options)):
            # Retourne le nombre
            return choice
        # Afficher message erreur
        print("Le choix n'est pas bon, vérifie")
        
# Afficher les options
def show_options(options):
    # Pour index, option in enumerees options
    for index, option in enumerate(options, start=1):
        # Afficher index + option
        print(f"{index}- {option}")


# Diriger en fonction du choix
def redirection_choice(choice, pseudo):
    # Si égal à 1
    if choice == "1":
        # Lancer la partie
        game.game_start(pseudo)
    # Elif égal à 2
    elif choice == "2":
        # Voir le classement
        game.show_ranking()
    # Sinon
    else:
        # Quitter le code
        sys.exit()
        

