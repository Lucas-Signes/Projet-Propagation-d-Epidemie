# Projet-Propagation-Epidemie
Simulateur de propagation d'epidemie - Lucas S et Quentin MlP
Version: Finale - 18/02/22
Le simulateur a 8 fichier qui continnent l'entierete du code pour assurer le fonctionnoment du simulateur.

Voici l'explication de chaque fichier et de ces contenus:

parametres_configuration[1, 2, 3] : 
Il ya trois fichiers nomme parametres_configuration1, parametres_configuration2, parametres_configuration3  
parametres_configuration1: Est un modele assez equilibre avec une densite de population initiale de cellule infecte de 1, une propagation modere, un taux de mort modere et avec 9 jours de guerison.
parametres_configuration2: Est un modele de basse porpagation mais avec un haut taux de mort avec une population initiale de cellule infecte de 1, une propagation basse, un taux de mort eleve et avec 10 jours de guerison.
parametres_configuration3: Est un modele de tres haute porpagation mais avec un taux de mort tres bas avec une population initiale de cellule infecte de 3, une propagation eleve, un taux de mort bas et avec 20 jours de guerison.

creation_config :
Ce fichier cree la configuartion initiale du simulateur, elle contient la fonction infection_init_pop. Elle se charge que par rapport a la densite de population intialement saine elle infecte le un nombre donne d'individus aleatoirement sur la grille

mise_a_jour :
Ce fichier calcule la prochaine iteration de le grille. La fonction tour_infect prend en charge l'augmentation de la valeur pour les cellules contamines. La fonction verification_mortalite_immunisation_guerison fait partie de l'extension du jeu de la vie realitse.
Elle verifier qu'apres un jour de mortalite donne, chaque jour qui suit, une cellule a un probabilite de mourrir donne, et si elle ne meurs pas apres un certain nombre de jour elle est guerri. L'extension d'imunite s'active entre la mort et la guerrison, apres un
certain nombres de jour donne une cellule est immunise, donc elle ne peut plus propager le virus, mais pendant cette periode d'immunite ell peut quand meme mourri. La fonction infection_pop verifie qu'apres chaque tour toute cellule infecte a une probabilite donner d'infecter
ces cellules voisines qui sont saines. Une extension de cette fonction est que les cellules infecte ont 2 fois moins de probabilite d'infecte leurs voisines en diagonale. La fonction compteur calule le nombre de cellule morte, gueris et non-infectes et l'affiche en nombre de cellule
et en pourcentage juste apres l'affichage de la grille en couleur.

affichage : 
Ce fichier se charge de l'affichage de le grille a chaque tour. Elle contient les fonction afficher_en_couleur et afficher_carre_couleur qui sont utilise par la fonction affichage_grille. Cette fonction traverse la liste et lui associe un carre simple en couleur 
pour chaque type de cellule. Une cellule grise veut dire qu'elle est: saine, Une cellule rouge veut dire qu'elle est: infecte, Une cellule verte veut dire qu'elle est: guerri, Une cellule jaune veut dire qu'elle est: immunise.

import_export :
Ce fichier prend une grille finale d'une simulation d'epidemie et la transforme en fichier .csv appele simulateur_epidemie.csv. Ce fichier peut alors etre utilise par la fonction fichier_vers_liste qui retranscrit ce fichier en liste. Dans ce fichier l'utilisateur est propose
de sauver sa simulation et si elle accepte elle est sauvegarder dans le fichier .csv .

epidemie : 
Ce fichier regroupe toute les fichier et les fonctions pour faire fonctionner le programme. Elle appelle les fonction infection_init_pop et l'affiche pour pour initialiser le simulateur. La fonction simulation_term verfie par rapport au cellule qui reste quand la simulation
se terminera. La fonction tour apelle les fonctions en affichant chaque jour qui se passe dans la simulation. La boucle d'appels se termine grace a la fonction simulation_term.

COMMENT CHOSIR SES PARAMETRES:
Le simulateur de propagation d'epidemie vient avec trois configuration de parametre. Pour chosir lequel vous souhaitez utilise changer le nom du fichier de paramtres que vous voulez chosir et echanger son numero avec la lettre "P" (representatif de la configuration de parametres principal)
Si vous souhaitez changer de fichier de configuration de prametres modifier le fichier en remplacant le P du fichier appeller actuellement parametres_configurationP avec son numero original et echanger le numerole du nouveau fichier que vous souhaitez utiliser avec la lettre "P".

COMMENT JOUER AVEC LA SIMULATION SANS SAUVEGARDER:
Pour jouer avec la simulation, sans vouloir sauvegarder son affichage finale, ouvrez touts les fichier (n'ouvrez que la configuartion de parametres chosi) et puis selectionnez le fichier epidemie avant de Run le programme.

COMMENT SAUVEGARDER UNE SIMULATION: 
Pour jouer avec la simulation mais en sauvegardans son affichage finale, ouvrez touts les fichier (n'ouvrez que la configuartion de parametres chosi) et puis selectionnez le fichier import_export avant de Run le programme. Quand vs etes porposez de sauvegarder insere la reponse
sois oui sois non.

Simulateur de propagation d'epidemie - Ecrit par Lucas Signes
