age = int(input("Quel est votre âge ?"))
maj_suisse = 18
maj_int = 21

if age > maj_int:
    print("Vous êtes majeur en Suisse et dans tous les pays du monde.")
elif age > maj_suisse and age < maj_int:
    print("Vous êtes majeur en Suisse, mais pas dans tous les pays du monde.")
else:
    print ("Vous n'êtes pas majeur en Suisse, ni dans les autres pays du monde.")
