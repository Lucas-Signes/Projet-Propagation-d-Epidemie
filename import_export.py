# FONCTIONS DE BASE POUR MANIPULER DES FICHIERS EN PYTHON
from epidemie import G
from parametres_configurationP import *

def creer_fichier(G, A, separateur = ";"):
    """
    Entrée : une liste de listes et une chaîne de caractères correspondante au nom d'un fichier
    Sortie : écriture des élements de la liste de liste L dans le fichier, ligne par ligne et élément par élément (séparés par un espace par défaut)
    """
    L = [[0 for i in range(x)] for j in range(y)]
    for i in range(1,x+1):
        for j in range(1, y+1):
            L[i-1][j-1] = G[i][j]
    grille = L
    
    F = open(A, "w")      #  on ouvre le fichier en mode "w" ("w" = mode écriture qui écrase le contenu déjà existant ; "r" = mode lecture seule ; "a" : mode append, qui rajoute le texte à la fin du fichier)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            F.write(str(grille[i][j]))      # on écrit le j-ème mot de la i-ème ligne de L
            if j < len(L[i]) - 1:
                F.write(separateur)
            F.write("\n")          # pour rajouter des sauts de ligne (s'ils ne sont pas déjà gérés dans le fichier)
    F.close()                       # il faut impérativement fermer le fichier pour qu'il soit bien sauvegardé

def fichier_vers_liste(A, separateur = ";"):
    """
    Entrée : une chaîne de caractères correspondante au nom d'un fichier
    Sortie : la liste des lignes du fichier, chaque ligne étant donnée sous forme de la liste de ses mots (séparés par un espace par défaut)
    """
    L = []
    try :
       with open(A, "r") as f:    # permet d'ouvrir un fichier et de le fermer automatiquement
            for ligne in f:                 # on parcourt l'ensemble du fichier (effectué ligne par ligne)
#                L.append(ligne)             # ajout de la ligne à la liste (ligne ajouté comme un unique élément)
                L.append(ligne.split(separateur)) # ligne.split() est une liste dont les éléments sont les mots de ligne, séparés par le caractère separateur
    except FileNotFoundError:               # au cas où le fichier n'existe pas (et dans ce cas, la liste reste vide et revient à créer un fichier vide)
        pass
    return L

def exporter_affichage():
    ver = input("Souhaitez vous garder cet affichage? : ")
    if ver == "oui":
        creer_fichier(G,'simulateur_epidemie.csv')
    elif ver == "non":
        pass
    else: 
        input("Souhaitez vous garder cet affichage? : ")
exporter_affichage()

L= fichier_vers_liste('simulateur_epidemie.csv')