class Perso:
        
    @staticmethod 
    def decompose_text(text):
        mots = text.split()                                          # Séparation du texte en mots en utilisant la méthode split
        espaces = " " * 51                                           # Longueur de chaque phrase vaut 51 caractères, ici 51 espaces
        phrases = []                                                 # Initialisation d'une liste pour les six phrases composant le textes
        phrase = ""                                                  # Initialisation de la chaîne de 51 caractères (comprise 6x dans la liste phrases)

        for mot in mots:  
            if len(phrase) + len(mot) <= 51:                        # Si la longueur de la phrase actuelle plus la longueur du mot actuel est inférieure ou égale à 51
                phrase += mot + " "                                 # Ajoute du mot actuel à la fin de la phrase avec un espace
            else:

            # Si la longueur de la phrase actuelle + la longueur du mot dépasse 51
            # La méthode str.rstrip() est utilisée pour supprimer les espaces à la fin de la chaîne. 
            # Ensuite, la méthode str.ljust() est utilisée pour remplir la chaîne avec des espaces à gauche jusqu'à atteindre une longueur de 51 caractères
                
                phrases.append(phrase.rstrip().ljust(51, " "))
                phrase = mot + " "                                  # La phrase précédente étant remplie, le mot est ajouté à la phrase suivante avec un espace

        if phrase:                                                  # Si il y a encore des mots dans la phase actuelle
            phrases.append(phrase.rstrip().ljust(51, " "))          # voir plus haut

        while len(phrases) < 6:
            phrases.append(espaces)                                 # Ajout d'une chaîne de 51 espaces à la liste des phrases si celle-ci n'est pas composé de 6 phrases

        return tuple(phrases[:6])                                   # Renvoie les six premiers éléments de la liste des phrases sous forme de tuple

