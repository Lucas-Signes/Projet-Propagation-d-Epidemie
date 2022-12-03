from parametres_configurationP import *

def afficher_en_couleur(texte, couleur_texte = 'normal', couleur_fond = 'normal'):
    """
    Affichage d'un texte en couleur sur un fond d'une autre couleur
    """
    codes_couleurs = { 'normal': -30, 'noir': 0, 'rouge': 1, 'vert': 2, 'jaune': 3, 'bleu': 4, 'rose': 5, 'cyan': 6, 'gris': 7 }
    foreground = 30 + codes_couleurs[couleur_texte]
    if couleur_fond == 'normal':
        background = foreground
    else:
        background = 40 + codes_couleurs[couleur_fond]
    print("\033[{}m\033[{}m{}\033[0m".format(foreground, background, texte), end = "")

def afficher_carre_couleur(couleur):
    """
    Affichage d'un carré simple en couleur
    """
    afficher_en_couleur(" ", couleur, couleur)

def afficher_grille(x, y):
    """
    Parameters
    ----------
    x : la longeur de la liste
    y : l'hauteur de la liste

    Returns
    -------
    Cette fomction traverse la liste et pour chaque cellule saine, infecte, immunise ou morte, lui associe une couleur code et l'affiche en tant que carre simple en couleur

    """
    for i in range(1, x+1):
        for j in range(1, y+1):
            if G[i][j]["etat"] == "saine":
                print(" ", end="")
                afficher_carre_couleur("gris")
            elif G[i][j]["etat"] == "infecte":
                print(" ", end="")
                afficher_carre_couleur("rouge")
            elif G[i][j]["etat"] == "immunise":
                print(" ", end="")
                afficher_carre_couleur("jaune")
            elif G[i][j]["etat"] == "mort":
                print(" ", end="")
                afficher_carre_couleur("noir")
            elif G[i][j]["etat"] == "guerri":
                print(" ", end="")
                afficher_carre_couleur("vert")
        print("\n")
