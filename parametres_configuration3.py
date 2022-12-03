import random
x=20 #x est la variable parametrable pour la hauteur de la grille
y=20 #y est la variable parametrable pour la hauteur de la grille
G = [[{"etat": "saine", "valeur": 0} for i in range(x+2)] for j in range(y+2)] #G est une liste de listes de longeur x et d'hauteur y ou chaque celule est saine est a une valeur de 0

dinitpersinfect = 1
jguer = 20
longeurimmun = 3
jimmunite = 17
pinfect = 18
tmort = 3
jmort = 10
