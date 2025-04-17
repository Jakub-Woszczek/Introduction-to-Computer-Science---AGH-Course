def czy_max_i_min(N):
    import random
    tablica = []

    for _ in range(N):
        liczba = random.randint(1, 100)
        tablica.append(liczba)

    max_liczba = tablica[0]
    min_liczba = tablica[0]

    for i in range(0,N-1):
        if tablica[i]>max_liczba:
            max_liczba = tablica[i]

        else:
            if tablica[i] <min_liczba:
                min_liczba = tablica[i]

    return min_liczba,max_liczba,tablica

print(czy_max_i_min(20))