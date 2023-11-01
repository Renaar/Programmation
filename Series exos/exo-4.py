print("== Chatbot ==\n")

chatbot_response = "Bot ==> "


def chatbot():
    salut = input("Humain : ")
    if salut.lower() == "bonjour":
        print(chatbot_response + "Coucou toi !\n")
        return chatbot()

    elif salut.lower() == "qui t'a créé ?":
        print(chatbot_response + "Ceci est une information classée Secret Defense... Désolé mon chou.\n")
        return chatbot()

    else:
        print(chatbot_response + "Je ne comprends pas la question.\n")
        return chatbot()


chatbot()
