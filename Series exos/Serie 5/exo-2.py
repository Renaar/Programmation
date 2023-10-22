n = int(input("Combien de nombres ? "))
counter = 0

for i in range(2, n*10):
    for j in range(2, int(i / 2) + 1):
        if (i % j) == 0:
            break
    else:
        print(i)
        counter += 1
        if counter == n:
            break
        else:
            continue
