import random
tablica = [1,3,4,3,3,5,7,9]

def spójny_podciąg_rosnący(N):

    # for _ in range(N):
    #     liczba = random.randint(1, 5)
    #     tablica.append(liczba)


    długość_max = 0
    for i in range(N-1):
        prev = i
        next = i+1

        długość = 1
        suma_el = 0
        suma_indexów = 0
        suma_el += tablica[prev]
        suma_indexów += i

        while tablica[prev] < tablica[next]:

            suma_el += tablica[next]
            i += 1
            suma_indexów += i
            długość +=1
            prev +=1
            next +=1

            if next>N-1:
                break

        if suma_el == suma_indexów:
            długość_max = długość

    return długość_max,tablica


print(spójny_podciąg_rosnący(len(tablica)))