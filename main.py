# Afficher le menu
    # Demander le pseudo
    # tant que vrai
        # Demander un choix valide
        # Si diriger en fonction du choix égal Faux
            # Break

# Demander le pseudo
    # Tant que vrai
        # Demander un pseudo
        # Si le pseudo est utilisé
            # Ajouter pseudo à la bdd
            # Retourne pseudo
        # Affichage erreur
            
        
# pseudo utilisé
    # Si pseudo est dans liste pseudo
        # Retourne Faux
    # Retourne True

# Demander un choix valide
    # Tant que vrai
        # Afficher les options
        # Demander un choix
        # Si nombre est valide parmi les options
            # Retourne le nombre
        # Afficher message erreur
    
# Afficher les options
    # Pour index, option in enumerees options
        # Afficher index + option
        
# Nombre valide parmis les options
    # Si le choix n'est un nombre
        # Retourne Faux
    # Convertir en entier
    # Si le choix n'est compris entre le min et max
        # Retourne Faux
    # Retourne Vrai

# Diriger en fonction du choix
    # Si égal à 1
        # Lancer la partie
    # Elif égal à 2
        # Voir le classement
    # Sinon
        # Quitter
        
# Voir le classement
    # Chercher la liste avec pseudo + résultat
    # Pour index 10 fois
        # Chercher le plus au score dans la liste
        # Afficher le plus au score index+1 + pseudo + score
    
# Chercher le plus au score dans la liste
    # Creation du dic avec pseudo + score
    # Pour dic dans la liste
        # Trouver le max de la liste du dic
        # Si max de la liste supérieur à score
            # Remplacer le pseudo et le score
