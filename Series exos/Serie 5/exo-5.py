liste_nombre = []

liste_nombre.append(input("Entrez la valeur du numéro 1 : "))
liste_nombre.append(input("Entrez la valeur du numéro 2 : "))
liste_nombre.append(input("Entrez la valeur du numéro 3 : "))
liste_nombre.append(input("Entrez la valeur du numéro 4 : "))
liste_nombre.append(input("Entrez la valeur du numéro 5 : "))

for i in liste_nombre:
    if int(i) % 2 == 0:
        print(str(i) + " est pair.")
    if int(i) > 0:
        print(str(i) + " est positif.")
    carre_parfait = int(i) ** 0.5
    if int(i) > 0 and carre_parfait.is_integer():
        print(str(i) + " est un carré parfait.")
