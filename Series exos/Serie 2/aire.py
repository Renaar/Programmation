import math

def aire_carre():
    print("- Calcul de l'aire d'un carré -")
    cote = int(input("Quelle est la longueur du côté de carré (en cm) ? "))
    print("Le carré a une aire de " + str(cote ** 2) + " cm2.")

def aire_rectangle():
    print("- Calcul de l'aire d'un rectangle -")
    petit_cote = int(input("Quelle est la longueur du petit côté du rectangle (en cm) ? "))
    grand_cote = int(input("Quelle est la longueur du grand côté du rectangle (en cm) ? "))
    print("Le rectangle a une aire de " + str(petit_cote * grand_cote) + " cm2.")

def aire_cercle():
    print("- Calcul de l'aire d'un cercle -")
    rayon = int(input("Quel est le rayon du cercle (en cm) ? "))
    print("Le cercle a une aire de " + str(round(math.pi * rayon**2 , 2)) + " cm2.")

forme = str(input("De quelle forme souhaitez-vous calculer l'aire ? [carre, rectangle, cercle] "))

if forme == str("carre"):
    aire_carre()

if forme == str("rectangle"):
    aire_rectangle()

if forme == str("cercle"):
    aire_cercle()
