# Lancer le jeux
    # Demander l'équipe
    # Tant que l'equipe est vivant
        # 
    
# Demander l'équipe
    # Création de l'équipe
    # Tant que l'équipe est inf à 3
        # Demander un personnage
        # Ajouter le personnage à l'equipe
    # Retourne l'équipe
        
# Demander un personnage
    # Tant que vrai
        # Afficher les options
        # Demander un choix
        # Si personnage est valide parmi les options
            # Retourne le nombre
        # Sinon 
            # Afficher message erreur
            
# Afficher les options
    # Pour index, option in enumerees options
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
        # Si personnage supérieur à 0
            # Retourne True
    # Retourne Faux