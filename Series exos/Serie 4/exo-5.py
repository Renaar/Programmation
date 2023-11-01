import random
print("== Chatbot ==\n")

chatbot_response = "Bot ==> "
chatbot_name = ''
historique = []


def chatbot():
    global chatbot_response
    global historique
    salut = input("Humain : ")
    if salut.lower() == "bonjour" or salut.lower() == "salut" or salut.lower() == "coucou":
        print(chatbot_response + "Coucou toi !\n")
        return chatbot()

    elif salut.lower() == "qui es tu ?":
        print(chatbot_response + "L'important n'est pas de savoir qui je suis, mais de savoir ce qu'on mange à midi.\n")
        return chatbot()

    elif salut.lower() == "qui t'a créé ?":
        print(chatbot_response + "Ceci est une information classée Secret Defense... Désolé mon chou.\n")
        return chatbot()

    elif salut.lower() == "ca va ?":
        print(chatbot_response + "Ca va, ca va, Imotep.\n")
        return chatbot()

    elif salut.lower() == "quel est ton nom ?" or salut.lower() == "comment tu t'appelles ?":
        global chatbot_name
        if chatbot_name == '':
            chatbot_response = "Bot ==> "
            print(chatbot_response + "C'est une très bonne question...")
            chatbot_name = input(chatbot_response + "Je peux être qui tu veux mon chou, choisis-moi un nom : ")
            print(chatbot_response + "Très bien, je suis désormais " + chatbot_name.title() + "\n")
            chatbot_response = chatbot_name.title() + " ==> "
            return chatbot()
        else:
            print(chatbot_response + "Je m'appelle " + chatbot_name + ".")
        return chatbot()

    elif salut.lower() == "shifumi":
        shifumi()

    else:
        print(chatbot_response + "Je ne comprends pas la question.\n")
        return chatbot()


def shifumi():
    human_choice = input(chatbot_response + "Que choisis-tu ? (pierre, feuille, ciseau) : ")
    rand_numb = random.randint(1, 3)  # pierre = 1 ; feuille = 2 ; ciseau = 3

    if human_choice == "pierre" and rand_numb == 1:
        print(chatbot_response + "Pierre\nMatch nul !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "pierre" and rand_numb == 2:
        print(chatbot_response + "Feuille\nPERDU ! AH AH AH !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "pierre" and rand_numb == 3:
        print(chatbot_response + "Ciseau\nT'as gagné, bien joué !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "feuille" and rand_numb == 2:
        print(chatbot_response + "Feuille\nMatch nul !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "feuille" and rand_numb == 3:
        print(chatbot_response + "Ciseau\nPERDU ! AH AH AH !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "feuille" and rand_numb == 1:
        print(chatbot_response + "Pierre\nT'as gagné, bien joué !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "ciseau" and rand_numb == 3:
        print(chatbot_response + "Ciseau\nMatch nul !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "ciseau" and rand_numb == 1:
        print(chatbot_response + "Pierre\nPERDU ! AH AH AH !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    elif human_choice == "ciseau" and rand_numb == 2:
        print(chatbot_response + "Feuille\nT'as gagné, bien joué !\n")
        revanche = input(chatbot_response + "Revanche ? (o/n): ")
        if revanche == 'o':
            return shifumi()
        else:
            return chatbot()

    else:
        print(chatbot_response + "Je n'ai pas compris ton choix...")
        return shifumi()


chatbot()
