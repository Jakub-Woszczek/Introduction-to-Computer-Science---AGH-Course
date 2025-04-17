import random

def czy_liczba_ma_wszystkie_nieparzyste(num):
    while num !=0:
        reszta = num % 10
        if reszta % 2 == 0:
            return False
        num //= 10

    return True




def czy_w_tabliczby_el_z_nieparzystą(N):
    tablica_t = []

    for i in range(N):
        liczba = random.randint(1,1000)
        tablica_t.append(liczba)

    for m in range(N):

        if czy_liczba_ma_wszystkie_nieparzyste(tablica_t[m]) ==True:
            print(tablica_t)
            return True
    print(tablica_t)
    return False

print(czy_w_tabliczby_el_z_nieparzystą(10))