import random

def czy_liczba_ma_nieparzystą(num):
    while num !=0:
        reszta = num % 10
        if reszta % 2 != 0:
            return True
        num //= 10

    return False




def czy_w_tabliczby_el_z_nieparzystą(N):
    tablica_t = []

    for i in range(N):
        liczba = random.randint(1,1000)
        tablica_t.append(liczba)

    for m in range(N):

        if czy_liczba_ma_nieparzystą(tablica_t[m]) ==False:
            print(tablica_t)
            return False
    print(tablica_t)
    return True

print(czy_w_tabliczby_el_z_nieparzystą(10))