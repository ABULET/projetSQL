import tkinter
import os
import sqlite3


def lire_requetes(fichier):
    """
    Importe une requête et la met dans une liste vide
    Argument:
        fichier: un fichier.txt contenant une requete sql
    Renvoi:
        Liste: une liste
    """
    assert type(fichier) == str
    Liste = []
    with open(fichier,"r") as requete:
        lignes = filin.readlignes()
        for ligne in lignes:
            Liste.append(ligne)
    return Liste


def ajouter_requetes(dico,fichier):
    """
    ajoute une requête sous forme de liste dans un dictionnaire
    Arguments:
        fichier: un fichier.txt contenant une requete sql
        dico: un dictionnaire contenant une/des requete(s)(il peut etre vide)
    Renvoi:
        dico: un dictionnaire contenant au moins un requete
    """
    assert type(dico) == dict
    dico.append(lire_requetes(fichier))
    return dico



def afficher_table(table, titre ="", debut = 0, fin = None):
	"""
	Affiche une table.
	Arguments:
		table: une liste de tuples
		titre: str du titre à afficher avant la table
		debut: indice de la première ligne que l'on veut afficher
		fin: indice de la dernière ligne que l'on veut afficher
			si fin est à None, on affiche jusqu'à la dernière ligne
	Renvoi:
		rien
	"""
	if titre != "":
		titre = titre + "\n\n"
	#print(titre + texte_table(table, debut, fin))
	affichage(titre + texte_table(table, debut, fin), titre)


def affichage(texte, titre = "Requêtes tables"):
	"""
	Affiche un texte (résultat d'une requête)
	Arguments:
		texte: str du texte à afficher
		titre: str du titre de la fenêtre
	Renvoi:
		rien
	"""
	root = tkinter.Tk()
	root.title(str(titre))
	RWidth=root.winfo_screenwidth() - 100
	RHeight=root.winfo_screenheight() - 100
	root.geometry("%dx%d+50+0"%(RWidth, RHeight))
	text=tkinter.Text(root, wrap = 'none')
	scroll_x=tkinter.Scrollbar(text.master, orient='horizontal', command = text.xview)
	scroll_x.config(command = text.xview)
	text.configure(xscrollcommand = scroll_x.set)
	scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
	scroll_y = tkinter.Scrollbar(text.master)
	scroll_y.config(command = text.yview)
	text.configure(yscrollcommand = scroll_y.set)
	scroll_y.pack(side = tkinter.RIGHT, fill = 'y')
	text.insert("1.0", texte)
	text.pack(side = tkinter.LEFT, expand = True, fill = tkinter.BOTH)
	root.mainloop()

table = []
for i in range(3,10):
    ajouter_requetes(table,"req",i,".txt")

afficher_table(table,"titre",0,7)
