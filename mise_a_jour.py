from parametres_configurationP import *

def tour_infect(x, y):
  """
    Parameters
    ----------
    x : la longeur de la liste
    y : l'hauteur de la liste

    Returns
    -------
    Traverse la liste et pour chaque cellule infecte ou immunise augmente ca valeur de 1 pour indiquer le nombre de jour depuis quil a ete contamine
    """
  for i in range(1,x+1):
    for j in range(1,y+1):
        if G[j][i]["etat"] == "infecte" or G[j][i]["etat"] == "immunise":
            G[j][i]["valeur"] = G[j][i]["valeur"] + 1
 
def verification_mortalite_immunisation_guerison(tmort, jmort, jguer, jimmunite, longeurimmun):
    """
    Parameters
    ----------
    tmort : le taux de mort
    jmort : le nombre de jour apres lequel une cellule peut mourrir
    jguer : le nombre de jour apres lequel une cellule sera gueri
    jimmunite : le nombre de jour apres lequel une cellul est immunise
    longeurimmun : le nombre de jour qu'une cellul est immunise

    Returns
    -------
    Cette fonction fait evoluer laffichage de 3 maieres differentes, il traverse la liste et si le jour de mortalite est atteint chaque jour suivant une cellule infecte a une certaine probabilite de mourrir.
    si le jour d'immunisation est atteint la cellule est immunise pendant un duree d'immunuite donner, lors de cette periode la cellule ne peut plus etre infect ni infecte d'autre cellule mais peut quand meme mourrir.
    si le jour de guerison est atteint la cellule est alors guerise
    """
    for i in range(1,x+1):
        for j in range(1, y+1):
            if G[j][i]["valeur"] >= jmort and G[j][i]["etat"] == "infecte" or G[j][i]["etat"] == "immunise":
                d = random.randint(1, 100)
                if d <= tmort:
                    G[j][i]["etat"] = "mort"
            if G[j][i]["etat"] != "mort" and G[j][i]["valeur"] == jimmunite and G[j][i]["valeur"] < longeurimmun + jimmunite:
                G[j][i]["etat"] = "immunise"
            if G[j][i]["valeur"] >= jguer and G[j][i]["etat"] != "mort":
                G[j][i]["etat"] = "guerri"
            

def infection_pop(x, y, pinfect):
    """
    Parameters
    ----------
    x : la longeur de la liste
    y : l'hauteur de la liste
    pinfect : probabilite d'infection

    Returns
    -------
    Cette fonction fait evoluer la propagation du virus. Il traverse la liste et si une cellule est infecte alors il ya une probabilite d'infection qui est applique a toutes ces voisines, celle de diagonale on 2 fois moins de chance detre infecte.
    Si les cellules voisines sont infece alors leur etat change a celui d'une cellule infecte qui peut elle meme infecte ces vosine le tour suivant 
    """
    for i in range(1, x+1):
      for j in range(1, y+1):
        if G[j][i]["etat"] == "infecte":
            c1 = random.randint(0,99)
            c2 = random.randint(0,99) 
            c3 = random.randint(0,99)
            c4 = random.randint(0,99)            
            if c1 < pinfect and G[j][i-1]["etat"] == "saine":
                G[j][i-1]["etat"] = "infecte"
            if c2 < pinfect and G[j][i+1]["etat"] == "saine":
                G[j][i+1]["etat"] = "infecte"
            if c3 < pinfect and G[j+1][i]["etat"] == "saine":
                G[j-1][i]["etat"] = "infecte"
            if c4 < pinfect and G[j-1][i]["etat"] == "saine":
                G[j+1][i]["etat"] = "infecte"
            d1 = random.randint(0,199)
            d2 = random.randint(0,199) 
            d3 = random.randint(0,199)
            d4 = random.randint(0,199)            
            if d1 < pinfect and G[j-1][i-1]["etat"] == "saine":
                G[j-1][i-1]["etat"] = "infecte"
            if d2 < pinfect and G[j-1][i+1]["etat"] == "saine":
                G[j-1][i+1]["etat"] = "infecte"
            if d3 < pinfect  and G[j+1][i-1]["etat"] == "saine":
                G[j+1][i-1]["etat"] = "infecte"
            if d4 < pinfect  and G[j+1][i+1]["etat"] == "saine":
                G[j+1][i+1]["etat"] = "infecte"
                
def compteur(x, y):
    """
    Parameters
    ----------
    x : la longeur de la liste
    y : l'hauteur de la liste

    Returns
    -------
    Cette fonction traverse la liste et affiche le nombre de morts, de gueris et de non-infectes, et donne egalement leurs pourcentages
    """
    M = 0
    R = 0
    N = 0
    for i in range(1, x+1):
        for j in range(1, y+1):
            if G[i][j]["etat"] == "mort":
                M = M+1
            if G[i][j]["etat"] == "guerri":
                R = R+1
            if G[i][j]["etat"] == "saine":
                N = N+1
    print(" Il ya", M, "morts, soit", round((M/(x*y))*100, 2), "% \n Il ya", R, "gueris, soit", round((R/(x*y))*100, 2), "% \n Il ya", N, "non-infectes, soit", round((N/(x*y))*100, 2), "%" )
