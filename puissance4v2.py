﻿def creer_grille():
#cré un grille de puissance 4 vide sous la forme d'un tableau
    grille = []
    for k in range(6):
        grille.append([0]*7)
    return grille


def afficher_grille(grille):
#affiche la grille de puissance 4 de manière lisible
    for n in range(6):
        print(grille[n])
    print(" ")



def est_dans(nombre,liste):
    #renvoie true si le nombre est dans la liste sinon False
    if len(liste) == 0:
        return False
    else:
        for k in range(len(liste)):
            if liste(k) == nombre:
                return True
        return False



def ajouter_pion(grille,colonne,num):
#remplace le 0 le plus bas de la colonne par le nombre num
#une colonne est remplie quand elle ne contient plus aucun 0(donc lorsque le plus haut élement de la colonne est positif)
#renvoie true si la colonne est remplie et false si la colonne a encore de la place
    #si la colonne est complétement remplie
    if grille[0][colonne] != 0:
        print("cette colonne est déja remplie")
        return True
    #si il reste des places dans la colonne
    else:
        n = 5
        while grille[n][colonne] != 0:
            n = n-1
        grille[n][colonne] = num
        return False


def jouer():
#permet au joueur num de remplacer le 0 de leur choix par leur nombre l'un après
    num = 1
    grille = creer_grille()
    victoire = False
    #se répète tant que personne n'as gagné
    while victoire == False:
        grille2 = grille
        remplie = True
        print("joueur",num,", c'est à vous")
        #se répète tant que le numéro qu'as entré le joueur est "mauvais"
        while remplie == True:
            colonne = int(input())
            if colonne >= 0 and colonne <=6:
                remplie = ajouter_pion(grille,colonne,num)
            else:
                print("cette colonne n'existe pas,vous devez choisir un numéro en un numéro entre 0 et 6")
        num = num % 2 + 1
        afficher_grille(grille)


jouer()