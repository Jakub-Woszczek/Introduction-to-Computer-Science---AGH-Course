def czy_w_liście_0(list):

    for i in range(len(list)):
        if list[i] == 0:
            return True
    return False


def wiersz_i_kolumna_jedno_zero(N):
    import random

    T = [[random.randint(0, 1) for _ in range(N)] for _ in range(N)]

    for bruh in T:
        print(bruh)


    for wiersz in range(len(T)):
        lista_tymczasowa = [0 for _ in range(len(T))]
        for iterator in range(len(T)):
            liczpa = T[wiersz][iterator]
            lista_tymczasowa[iterator] = liczpa

        if czy_w_liście_0(lista_tymczasowa) == False:
            return False


    for kolumna in range(len(T)):
        lista_tymczasowa = [0 for _ in range(len(T))]
        for iterator in range(len(T)):
            liczpa = T[iterator][kolumna]
            lista_tymczasowa[iterator] = liczpa

        if czy_w_liście_0(lista_tymczasowa) == False:
            return False
    return True

print(wiersz_i_kolumna_jedno_zero(4))