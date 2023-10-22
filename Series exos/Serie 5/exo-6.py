

def entier_naturel(n: int):
    counter = 0
    l_1 = []
    l_2 = []
    l_3 = []
    if int(n) < 0:
        print("La valeur entrée n'est pas un entier naturel !")
        entier_naturel(int(input("Entrez un entier naturel : ")))
    for i in range(1, int(n + 1)):
        l_1.append(i)

    for i in range(2, n * 10):
        for j in range(2, int(i / 2) + 1):
            if (i % j) == 0:
                break
        else:
            l_2.append(i)
            counter += 1
            if counter == n:
                break
            else:
                continue
    for i in range(len(l_1)):
        l_3.append(l_2[i] - l_1[i])
    print(l_3)


entier_naturel(int(input("Entrez un entier naturel : ")))
