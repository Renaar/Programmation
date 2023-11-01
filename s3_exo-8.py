nb_max = int(input("Nombre max : "))
fibo_a = 1
fibo_b = 1
fibo_c = 0
count = 1

print(fibo_a)

while fibo_a < nb_max:
    fibo_c = fibo_a + fibo_b
    fibo_a = fibo_b
    fibo_b = fibo_c
    count += 1
    print(fibo_a)

print("Maximum atteint en " + str(count) + " coups.")