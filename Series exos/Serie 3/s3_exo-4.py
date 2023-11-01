pieces = int(input("Combien y a-t-il de pièces dans le coffre ? "))
matelots = int(input("Combien y a-t-il de matelots à bord ? "))

butin = pieces // (matelots + 1)
bonus = pieces & (matelots + 1)

print("Les pirates prennent chacun " + str(butin) + " pièces.")
print("Le capitaine prend un bonus de " + str(bonus) +  " pièces, soit un total de " + str(butin+bonus) + " pièces d'or")
