from parametres_configurationP import *
from creation_config import *
from mise_a_jour import *
from affichage import *

infection_init_pop(dinitpersinfect) #appelle la fonction pour initialiser la densite de cellules infectes
afficher_grille(x, y) #affiche la premiere iteration de la grille

def simulation_term(x, y ):
    """
    Parameters
    ----------
    x : la longeur de la liste
    y : l'hauteur de la liste

    Returns
    -------
    Cette fonction traverse la liste et verifier si il reste des cellules infectes et immunise dans l'affiche et retourne une reponse booleen. Si il ya toujour ce genre de cellule elle retourne faux et sinon elle retourn faux

    """
    fin = 0
    for i in range(1, x+1):
        for j in range(1, y+1):
           if G[i][j]["etat"] == "infecte" or G[i][j]["etat"] == "immunise":
               fin = fin+1
    if fin > 0:
        return False
    if fin == 0:
        print("La simulation est terminée")
        return True

def tour():
    """
    Parameters
    ----------
    NONE

    Returns
    -------
    Cette fonction appelle toutes les fonctions en appelant tout les autres fichier pour montrer progressivement l'affichage. Elle utilise la fonction simulation_term pour verifier quand ce finit la fonction pour savoir combien de fois elle doit repeter l'affichage.
    Chaque tour elle affiche le jour suivant et l'affichage evolue progressivement en terme de cellulle infecte, vague d'infections, immunisation et de guerrison
    """
    j = 1
    while simulation_term(x, y) == False:
        j = j+1
        print("\n Jour:", j)
        verification_mortalite_immunisation_guerison(tmort, jmort, jguer, jimmunite, longeurimmun)
        infection_pop(x, y, pinfect)
        tour_infect(x, y)
        afficher_grille(x, y)
        compteur(x, y)
tour()

                      