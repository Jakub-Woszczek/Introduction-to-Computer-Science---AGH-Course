import random

def  czy_nieparzysta(num):
    if num%2==0:
        return False
    else:
        return True

def nieparzysty_podciąg_palindrom(N):
    tablica = []

    for _ in range(N):
        liczba = random.randint(1, 5)
        tablica.append(liczba)
    print(tablica)
    prev = 0
    present = 1
    next = 2

    max_cunt = 0
    for _ in range(N-2):
        iterator = 1
        tablica_podciagów = []
        if tablica[prev] == tablica[next] and tablica[present]%2==1 and tablica[prev]%2==1 and  tablica[next]%2==1:
            cunt = 3
            tablica_podciagów.append(tablica[present])
            while tablica[prev-iterator] == tablica[next+iterator]:
                if  tablica[prev-iterator]%2==1 and tablica[next+iterator]%2==1:
                    tablica_podciagów.append(tablica[next+iterator])
                    tablica_podciagów = [tablica[prev-iterator]] + tablica_podciagów
                    cunt += 2
                iterator += 1


            if cunt > max_cunt:
                max_cunt = cunt




        if tablica[prev] == tablica[present] and tablica[prev]%2==1 and tablica[present]%2==1:
            cunt = 2
            tablica_podciagów.append(tablica[prev])
            tablica_podciagów.append(tablica[present])
            while tablica[prev-iterator] == tablica[present+iterator]:

                if tablica[prev-iterator]%2==1 and tablica[present+iterator]%2==1:
                    tablica_podciagów = [tablica[prev - iterator]] + tablica_podciagów
                    tablica_podciagów.append(tablica[present+iterator])
                    cunt +=2
                iterator += 1
            if cunt>max_cunt:
                max_cunt =cunt

        prev += 1
        present += 1
        next += 1

    return max_cunt,tablica_podciagów

print(nieparzysty_podciąg_palindrom(100))
