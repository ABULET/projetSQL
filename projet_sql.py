import tkinter
import os
import sqlite3

def charger_sql(table):
    #charge des tables
    conn = sqlite3.connect("imdb.db")
    c = conn.cursor()
    c.execute("select * from table")
    for row in c:
        print(row)
    conn.close()

def lire_requetes(dico,fichier):
    #importe des requetes et les mets sous forme d'un dictionaire
    with open(fichier,"r") as requete:
        lignes = filin.readlignes()
        for ligne in lignes:
            dico.append(ligne)
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
		titre += "\n\n"
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
