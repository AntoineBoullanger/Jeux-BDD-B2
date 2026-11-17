MAX_CHARACTERS = 3

# Lancer la partie
def game_start(pseudo):
    # Creation variable manche
    round = 0
    # Creer l'équipe
    team = create_team()
    # Tant equipe vivant
        # Incrémentation de 1 la variable manche
        # Affichage Manche
        # Lancer la manche
    # Afficher le résultat
    # Enregistrer le résultat dans la bdd

# Creer l'équipe
def create_team():
    # Création de la liste équipe
    list_team = []
    # Tant que taille de l'équipe est pas pleine
    while len(list_team) < MAX_CHARACTERS:
        # Afficher l'équipe
        show_team(list_team)
        # Demander un personnage
        # Ajouter le personnage à l'equipe
        # Supp le personnage de la liste de choix
    # Retourne l'équipe

# Afficher l'équipe
def show_team(list_team):
    # Pour index, personnage dans enumerate l'équipe
    for index, character in enumerate(list_team):
        # Afficher index + personnage
        print(f"{index+1}- {character["name"]} --- {character["ATK"]} - {character["DEF"]} - {character["PV"]} ")

# Demander un personnage
    # Tant que vrai
        # Afficher les options
        # Demander un choix
        # Si choix est valide parmi les options
            # Retourne le nombre
        # Sinon 
            # Afficher message erreur
            
# Afficher les options
    # Liste des personnages (allié)
    # Pour index, option in enumerees personnage
        # Afficher index + option
    
# Choix deja choisi
    # Si  nom du personnage dans equipe
        # Retourne Vrai
    # Retourne Faux

# équipe vivant ?
    # Pour personnage dans equipe
        # Si PV personnage supérieur à 0
            # Retourne True
    # Retourne Faux

# Lancer la manche
    # Creation de l'ennemis
    # Tant que equipe vivant
        # Attaque du Joueur
        # Si pas equipe vivant (ennemis)
            # break
        # Attaque Ennemis

# Creation de l'ennemis
    # Liste personnage (ennemis)
    # Retourne l'ennemis au hasard
    
# Attaque Joueur
    # Pour joueur dans l'équipe
        # Attaque le joueur
        
# Attaque le joueur
    # Si sup à 0
        # Enlever dégat 
        
        
# sup à n
    # Si pv supérieur à 0
        # retourne True
    # Retourne False
    
# Enlever dégat 
    # Compter les dégats
    # Afficher les dégats
    # Si sup à pv - deg
        # pv =- deg
    # Sinon
        # pv = 0
    

# Attaque Ennemis
    # Choisir un joueur au hasard parmis ce qui sont en vis
    # Compter les dégats
    # Afficher les dégats