# Lancer la partie
    # Creation variable manche
    # Demander l'équipe
    # Tant que l'equipe est vivant
        # Affichage Manche
        # Incrémentation de 1 la variable manche
        # Creation de l'ennemis
        # Lancer la manche

    
# Demander l'équipe
    # Création de l'équipe
    # Tant que l'équipe est inf à 3
        # Afficher l'équipe
        # Demander un personnage
        # Ajouter le personnage à l'equipe
    # Retourne l'équipe

# Afficher l'équipe
    # Pour index, personnage dans enumerate l'équipe
        # Afficher index + personnage

# Demander un personnage
    # Tant que vrai
        # Afficher les options
        # Demander un choix
        # Si personnage est valide parmi les options
            # Retourne le nombre
        # Sinon 
            # Afficher message erreur
            
# Afficher les options
    # Liste des personnages (allié)
    # Pour index, option in enumerees personnage
        # Afficher index + option
        
# Nombre valide parmis les options
    # Si le choix n'est un nombre
        # Retourne Faux
    # Si le choix n'est compris entre le min et max
        # Retourne Faux
    # Si le choix est dèjà choisi
        # Retourne Faux
    # Retourne Vrai
    
# Choix deja choisi
    # Si personnage dans equipe
        # Retourne Vrai
    # Retourne Faux

# équipe vivant ?
    # Pour personnage dans equipe
        # Si PV personnage supérieur à 0
            # Retourne True
    # Retourne Faux

# Creation de l'ennemis
    # Liste personnage (ennemis)
    # Retourne l'ennemis au hasard
    
# Lancer la manche
    # Attaque du Joueur
    # Si pas equipe vivant (ennemis)
        # break
    # Attaque Ennemis
    # Si pas equipe vivant (joueur)
        # break
        