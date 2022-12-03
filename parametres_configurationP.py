import random
x = 5 #x est la variable parametrable pour la hauteur de la grille
y = 5 #y est la variable parametrable pour la hauteur de la grille
G = [[{"etat": "saine", "valeur": 0} for i in range(x+2)] for j in range(y+2)] #G est une liste de listes de longeur x et d'hauteur y ou chaque celule est saine est a une valeur de 0

dinitpersinfect = 1 #la densite intiale de la population qui est infecte
jguer = 9 #le nombre de jour apres lequel une cellule est gueri
jimmunite = 6 #le nombre de jour apres lequel une cellule est immunise
longeurimmun = 3 #la duree qu'une cellule est immuniuse
pinfect = 11 #la probabilite qu'une cellule infecte, infecte ces voisines
jmort = 4 #le nombre de jours apres lequel une cellule peut mourrir
tmort = 5 #le teaux de mort dune cellule jusqua qu'elle est guerri
