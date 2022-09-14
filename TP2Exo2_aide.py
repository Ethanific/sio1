from random import *

nb_essai = 4  # valeur réelle : 10
MAX = 15      # valeur réelle : 1000

resultat = randint(1,MAX)
print(resultat) #utile pour les tests
compteur=0
print('Un nombre entre 1 et', MAX, 'est choisi : vous avez', nb_essai, 'essais pour le deviner')

gagne = False #initialement, le joueur n'a pas (encore) gagné


while not gagne :
    message = 'Essai n°' + str(compteur) + ' : '
    n=int(input(message))
    
