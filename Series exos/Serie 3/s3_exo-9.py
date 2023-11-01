nb = int(input("Indiquez un nombre : "))
count = 0                       #Initialisation de mon compteur à 0

while nb != 1:
    if (nb % 2 == 0):           #Je vérifie si nb est pair
        nb = int(nb / 2)        #Je le met en int pour éviter d'avoir des x.0 à chaque fois...
        count += 1
        print(nb)

    else:                       #Si nb n'est pas pair, il est impair... Logique...
        nb = int(nb * 3 + 1)    #évitons les x.0...
        count += 1
        print(nb)

print("Fin atteinte en " + str(count) + " coups.")