import math

calcul = int(input("Souhaitez vous calculer : \n1) Une aire\n2) Un volume\n Réponse : "))

if calcul == 1:
    forme_A = int(input("Souhaitez vous : \n1) Un rectangle\n2) Un disque\nRéponse : "))

    if forme_A == 1:
        g_cote = int(input("Grand côté (en cm): "))
        p_cote = int(input("Petit côté (en cm): "))
        print("Le rectangle a une aire de " + str(round((g_cote*p_cote), 2)) + "cm².")
    elif forme_A == 2:
        rayon_disc = int(input("Rayon du disque (en cm) : "))
        print("Le disque a une aire de " + str(round((math.pi * rayon_disc * rayon_disc), 2)) + "cm².")
    else:
        print("Instruction non comprise.")

elif calcul == 2:
    forme_B = int(input("Souhaitez vous : \n1) Un parallelepipède\n2) Une sphère\nRéponse : "))

    if forme_B == 1:
        longueur = int(input("Longueur du parallelepipède (en cm) : "))
        hauteur = int(input("Hauteur du parallelepipède (en cm) : "))
        profondeur = int(input("Profondeur du parallelepipède (en cm) : "))
        print("Le parallelepipède a un volume de " + str(round((longueur * hauteur * profondeur), 2)) + "cm³.")
    elif forme_B == 2:
        rayon_sphere = int(input("Rayon de la sphère (en cm) : "))
        print("La sphère a un volume de " + str(round(((4/3)* math.pi * (rayon_sphere ** 3)), 2)) + "cm³.")
    else:
        print("Instruction non comprise")
else:
    print("Instruction non comprise")