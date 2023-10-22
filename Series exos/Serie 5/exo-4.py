liste_note = []


def ajouter_note():
    stop = "fin"
    note = str(input("Ajouter une note : "))
    if note != stop:
        liste_note.append(float(note))
        ajouter_note()
    else:
        print("")
        print("La note maximale est : " + str(max(liste_note)))
        print("La note minimale est : " + str(min(liste_note)))
        print("La moyenne est : " + str(sum(liste_note)/len(liste_note)))


ajouter_note()
