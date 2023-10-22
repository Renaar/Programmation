a = float(input("Entrez le coefficient de degré 2 (a) : "))
b = float(input("Entrez le coefficient de degré 1 (b) : "))
c = float(input("Entrez le coefficient de degré 0 (c) : "))

print("Nous allons déterminer les racines réelles du polynome : " + str(a) + "x²+" + str(b) + "x+" + str(c) + ".")

disc = (b*b) - (4*a*c)
x1 = (-b - (disc**0.5)) / (2*a)
x2 = (-b + (disc**0.5)) / (2*a)

if disc > 0:
    print("Le polynome a deux racines réelles : " + str(x1) + " et " + str(x2))
elif disc == 0:
    print("Le polynome a une seule racine réelle : " + str(-b / (2*a)))
else:
    print("Pas de racine réelle !")