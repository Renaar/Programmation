nom = input("Nom du joueur : ")
age = int(input("Âge du joueur : "))
matches_joues = int(input("Nombre de matches joués la saison dernière : "))
cout = float(input("Coût du joueur (en CHF) : "))
poste = input("Poste du joueur (attaquant, milieu, défenseur, gardien) : ")

if age < 28 and matches_joues >= 30 and cout <= 100000:
   
    if poste == "attaquant":
        buts_marques = int(input("Nombre de buts marqués la saison dernière : "))
        if buts_marques > 10:
            print("Nous embauchons " + nom + ".")
        else:
            print("Nous n'embauchons pas " + nom + ".")
    elif poste == "milieu":
        passes_cles = int(input("Nombre de passes clés réalisées la saison dernière : "))
        if passes_cles > 200:
            print("Nous embauchons " + nom + ".")
        else:
            print("Nous n'embauchons pas " + nom + ".")
    elif poste == "défenseur":
        plaques_realises = int(input("Nombre de plaqués réalisés la saison dernière : "))
        if plaques_realises >= 100:
            print("Nous embauchons " + nom + ".")
        else:
            print("Nous n'embauchons pas " + nom + ".")
    elif poste == "gardien":
        buts_encaisses = int(input("Nombre de buts encaissés la saison dernière : "))
        if buts_encaisses < 30:
            print("Nous embauchons " + nom + ".")
        else:
            print("Nous n'embauchons pas " + nom + ".")
    else:
        print("Poste invalide. Nous n'embauchons pas " + nom + ".")
else:
    print("Nous n'embauchons pas " + nom + ".")
