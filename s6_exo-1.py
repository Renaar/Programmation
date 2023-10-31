import random # Permet de créer un nombre aléatoire

n = random.randint( 1, 100) # n va stocker un nombre aléatoire entre 1 et 100

nb_joueurs = int(input("Combien de joueurs ? ")) # On demande le nombre de joueurs
liste_joueurs = [] # Crée la liste qui contiendra les joueurs
winner = ("x" ,101) # Crée la variable qui contiendra le gagnant

for i in range(nb_joueurs): # On demande aux joueurs leur nom et leur numéro
    joueur = (input("Nom du joueur : "), int(input("Quel est ton numéro ? "))) # tuple(nom , numéro)
    liste_joueurs.append(joueur)

for i in liste_joueurs:
    diff = abs(n - i[1])
    if diff < winner[1]:
        winner = (i[0], diff)

print("Le nombre secret est " + str(n) +". Le gagnant est " + winner[0] + ".")