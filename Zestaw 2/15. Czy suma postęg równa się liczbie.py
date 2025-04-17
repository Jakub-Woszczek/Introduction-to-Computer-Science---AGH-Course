def czy_suma_postęg_rowna_liczbie(N):
    lista = []
    for i in range(1, N + 1):
        num = i
        a = num

        liczba_cyfr = 0
        while a != 0:
            if a != 0:
                liczba_cyfr += 1
                a //= 10
        a = num
        suma_potęg = 0
        for i in range(1, liczba_cyfr):
            cyfry_pojedyńcze = a % 10

            suma_potęg += cyfry_pojedyńcze ** (liczba_cyfr)

            a //= 10
        suma_potęg += a ** (liczba_cyfr)



        if suma_potęg == num:
            lista.append(num)

    return lista

N = int(input("podaj N: "))

print(czy_suma_postęg_rowna_liczbie(N))



