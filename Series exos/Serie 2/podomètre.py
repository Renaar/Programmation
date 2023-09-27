steps = int(input("Combien de pas avez-vous fait aujourd'hui ? "))
length = int(input("Quelle est votre longueur de pas moyenne (en cm) ? "))

# Pas besoin de créer une variable spécifique pour calculer, calcul possible dans le print
print("Vous avez parcouru " + str((steps * length) / 100 / 1000) + " kilomètres. Bravo !")
