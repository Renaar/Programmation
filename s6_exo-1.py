import random # Permet de créer un nombre aléatoire

n = random.randint( 1, 100) # n va stocker un nombre aléatoire entre 1 et 100

nb_joueurs = int(input("Combien de joueurs ? ")) # On demande le nombre de joueurs
liste_joueurs = []
winner = ("x" ,101)

for i in range(nb_joueurs):
    joueur = (input("Nom du joueur : "), int(input("Quel est ton numéro ?\n")))
    liste_joueurs.append(joueur)

for i in liste_joueurs:
    diff = abs(n - i[1])
    if winner = (i[0], diff)



# print(liste_joueurs)