m = float(input("Entrez un nombre entier naturel : "))
i = 0

if m != int(m):
    print(str(m) + " n'est pas un entier naturel !")
elif m < 0:
    print(str(m) + " n'est pas un entier naturel !")
else:
    while i <= m:
        sum = 0
        j = 0
        while j < i:
            sum += j
            j += 1
        i += 1
        print(sum)
