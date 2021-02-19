def lire_requetes(dico,fichier):
    with open(fichier,"r") as requete:
        lignes = filin.readlignes()
        for ligne in lignes:
            dico.append(ligne)
    return dico

lire_requetes({},"req1.txt")