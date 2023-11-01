B = float(input("Veuillez entrer le montant initial en banque (CHF): "))
t = float(input("Veuillez entrer le taux intérêt du compte (%): "))
D = float(input("Veuillez entrer le débit annuel (CHF): "))
list = []
a1 = 0
compteurannees = 2022
m1 = B 
while a1 <= 20:
    compteurannees += 1
    list.append(compteurannees)
    x = list [-1]
    a1 += 1
    print("Le montant en banque en " + str(x) + ": " + str(m1) + " CHF.")
    m1 = m1 + m1 * t/100 - D