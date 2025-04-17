def max_podciąg(N):
    import random
    T = [[random.randint(1, 9) for _ in range(N)] for _ in range(N)]
    for bruh in T:
        print(bruh)
    suma_max = 0
    for wiersz in range(len(T)):
        suma = 0
        for kolumna in range(len(T)):
            suma += T[wiersz][kolumna]

        if suma>suma_max:
            suma_max = suma
            podicąg = f'wiersz {wiersz}'

    for kolumna in range(len(T)):
        suma = 0
        for wiersz in range(len(T)):
            suma += T[wiersz][kolumna]

        if suma > suma_max:
            suma_max = suma
            podicąg = f'wiersz {kolumna}'

    return suma_max,podicąg

print(max_podciąg(5))


