bibliotheque = {
    "2974BA" : "J.R.R Tolkien : La communauté de l'anneau",
    "8467CA" : "Georges Orwell : 1984",
    "3294BB" : "Maurice Leblanc : Arsène Lupin, Gentleman cambrioleur",
    "6522DA" : "Stephen Hawking : Une brève histoire du temps",
    "7754AE" : "Stendhal : Le Rouge et le Noir",
    "6532EE" : "Victor Hugo : Les Misérables",
    "6439AD" : "Georges Perec : La Disparition",
    "8232AB" : "Emile Zola : La bête humaine",
    "9871EA" : "Jean-Jacques Rousseau : Les Confessions",
    "2334DD" : "Jean-Jacques Rousseau : Discours sur l'origine et les fondements de l'inégalité parmi les hommes",
    "9838EA" : "J.K. Rowling : Harry Potter à l'école des sorciers",
    "5535BE" : "J.K. Rowling : Harry Potter et la Chambre des secrets",
    "2934AD" : "Christopher Paolini : Eragon",
    "7477ED" : "Antoine de Saint-Exupéry : Le Petit Prince",
    "7588AA" : "Guy de Maupassant : Bel-ami",
    "3523EC" : "Schiller : Der Handschuh",
    "2377CC" : "Goethe : Die Leiden des jungen Werthers",
    "8499ED" : "Grass : Die Blechtrommel",
    "8373AA" : "Frisch : Homo faber",
    "5666BA" : "Dürrenmatt : Die Physiker",
    "8847CC" : "Brecht : Die Dreigroschenoper",
    "9956BC" : "Hesse : Der Steppenwolf",
    "4334AC" : "Alexandre Dumas : Le Comte de Monte-Cristo",
    "8858CC" : "Virginia Woolf : une chambre à soi",
    "3734BC" : "Margaret Mitchell : Autant en emporte le vent",
    "8767AC" : "Boris Vian : L'écume des jours",
    "3253CC" : "Simone Veil : Une Vie",
    "7756CA" : "Françoise Sagan : Bonjour Tristesse",
    "5452AE" : "Simone de Beauvoir : Le deuxième sexe",
    "8764CE" : "William Shakespeare : Roméo et Juliette",
    "9878BB" : "Guy de Maupassant : Le Horla",
    "5469AC" : "Marcel Proust : À la recherche du temps perdu",
    "8886BC" : "François Rabelais : Gargantua"
}

emprunt = {}

while True:
    print(" ")
    print("=== Bibliothèque ===")
    print(" ")
    command = input("Que voulez faire ?\n"
                    "\"afficher\" pour afficher la liste des livres de la bibliothèque\n"
                    "\"emprunts\" pour afficher la liste des livres empruntés\n"
                    "\"ajouter\" pour ajouter un livre à la bibliothèque\n"
                    "\"supprimer\" pour supprimer un livre à la bibliothèque\n"
                    "\"rechercher\" pour rechercher un mot dans la bibliothèque\n"
                    "\"emprunter\" pour emprunter un livre dans la bibliothèque\n"
                    "\"rendre\" pour rendre un livre emprunté\n"
                    "\"fin\" pour terminer la requête\n"
                    "Commande : ")
    
    if command == "fin":
        break

    elif command == "afficher":
        count = 0
        print(" ")
        print(20 * "=")
        print("Contenu de la bibliothèque")
        print(20 * "=")
        print(" ")
        for i in bibliotheque:
            print("Clé : " + str(i))
            print("Titre : " + bibliotheque[i])
            print(" ")
            print(10 * "=")
            print(" ")
            count += 1
        print("Nombre de livres : " + str(count))

    elif command == "ajouter":
        bibliotheque[input("Référence : ")] = input("Titre : ")
    
    elif command == "supprimer":
        bibliotheque.pop("Référence à supprimer ? ")

    elif command == "rechercher":
        recherche = str(input("Quel mot recherchez-vous ? "))
        print(" ")
        for i in bibliotheque:
            if recherche in bibliotheque[i]:
                print("Référence : " + i)
                print("Titre : " + bibliotheque[i])
                print(" ")
                print(10 * "=")
    
    elif command == "emprunter":
        ref_emprunt = input("Référence du livre à emprunter : ")
        if ref_emprunt in emprunt:
            print(" ")
            print("Livre déjà emprunté.")
            print(" ")
            
        elif ref_emprunt in bibliotheque:
            emprunteur = (bibliotheque[ref_emprunt] , input("Nom de l'emprunteur : "))
            emprunt[ref_emprunt] = emprunteur
            bibliotheque.pop(ref_emprunt)
            print(" ")
            print(f"{emprunteur[1]} a emprunté le livre \"{(emprunt[ref_emprunt])[0]}\".")
            print(" ")

        else:
            print(" ")
            print("Cette référence n'existe pas.")
            print(" ")
    
    elif command == "rendre":
        ref_rendre = input("Référence du livre à rendre : ")
        if ref_rendre in emprunt:
            bibliotheque[ref_rendre] = (emprunt[ref_rendre])[0]
            emprunt.pop(ref_rendre)
            print(" ")
            print(f"Le livre \"{bibliotheque[ref_rendre]}\" a été rendu.")
        
        elif ref_rendre in bibliotheque:
            print(" ")
            print("Ce livre n'a pas été emprunté.")
            print(" ")

        else:
            print(" ")
            print("Le livre n'existe pas.")
            print(" ")

    elif command == "emprunts":
        if bool(emprunt) is False:
            print(" ")
            print("Aucun livre n'a été emprunté")
        else:
            print(" ")
            print(10 * "=")
            print("Livres empruntés")
            print(10 * "=")    
            for i in emprunt:
                print(" ")
                print(f"Référence : {i}\n"
                      f"Titre : {(emprunt[i])[0]}")
                print(" ")
                print(10 * "=")

    elif bool(bibliotheque.get(command)) is False:
        print(" ")
        print("Commande incorrecte.")