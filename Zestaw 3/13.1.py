tablica = [2,9,3,1,7,7,1,3,9,12,15]
długość_tablicy = len(tablica)
indeks_first = -1
indeks_last = długość_tablicy-1

max_count = 0
for _ in range(długość_tablicy):
    indeks_first += 1
    indeks_last = długość_tablicy - 1
    for _ in range(długość_tablicy):
        print(indeks_first,indeks_last)
        count = 0
        if tablica[indeks_first] == tablica[indeks_last] and indeks_last != indeks_first:
            a = indeks_first
            b = indeks_last
            while tablica[a] == tablica[b] and a<b:
                a += 1
                b -= 1
                count += 1

            if count>max_count:
                max_count = count
        indeks_last -=1

print(max_count)

