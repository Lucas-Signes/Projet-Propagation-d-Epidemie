from parametres_configurationP import *

def infection_init_pop(dinitpersinfect):
    """
    Parameters
    ----------
    dinitpersinfect : la densite initiale de cellule infecte

    Returns
    -------
    Cette fonction imrpime le premier jour, puis prend la densite initiale de cellule infecte et les infecte aleatoirement sur la grille et puis retourne cette nouvelle grille G avec les cellule maintenant infectes
    """
    print("\n Jour: 1")
    for k in range(dinitpersinfect):
        G[random.randint(1, x)][random.randint(1, y)]["etat"] = "infecte"
    return G