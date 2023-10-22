liste_course = []


def ajouter_course():
    stop = "fin"
    article = input("Ajouter : ")
    if article != stop:
        liste_course.append(article)
        ajouter_course()
    else:
        print("")
        print("Votre liste de courses contient : ")
        for x in liste_course:
            print(" • " + x)


ajouter_course()
