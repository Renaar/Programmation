hauteur = int(input("Hauteur du sapin ? "))

for i in range(hauteur):
    print((str((2 * i + 1) * "*")).center(2*hauteur+1, " "))

print(hauteur * "_" + "‖‖" + hauteur * "_")
