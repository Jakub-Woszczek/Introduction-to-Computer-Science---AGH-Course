def njamniejsza_liczba_z_tablicy(T):
    liczba = 0
    min_liczba = T[0]
    index_do_najmniejszej = 0
    for index in range(len(T)):
        liczba = T[index]

        if liczba < min_liczba:
            min_liczba = liczba
            index_do_najmniejszej = index
    return min_liczba,index_do_najmniejszej

def najwiękksza_liczba_z_tablicy(T):
    liczba = 0
    min_liczba = T[0]
    index_do_najmniejszej = 0
    for index in range(len(T)):
        liczba = T[index]

        if liczba > min_liczba:
            min_liczba = liczba
            index_do_najmniejszej = index
    return min_liczba



def przepisywanie_sigletony(N):
    import random
    tablica = [[0 for _ in range(N)]  for _ in range(N)]
    liczba_prev = 0
    j = 0
    i = 0

    while i < N:
        j = 0
        liczba = 1

        while j < N:
            liczba += random.randint(1,10)
            tablica[i][j] = liczba
            j +=1

        i +=1

    # tablica_ostatnich = []
    # for zmienna in range(N):
    #     liczba = tablica[zmienna][N]
    #     tablica_ostatnich.append(liczba)
    # największa_liczba = najwiękksza_liczba_z_tablicy(tablica_ostatnich)

    tablica_indexów = [0 for _ in range(N)]
    posortowana_lista_jedna = []
    for _ in range(N**2):
        wiersz = 0
        lista_tymczasowa_do_wyboru = []
        for iterator in range(N):
            wiersz = iterator
            index_z_tab_index = iterator
            if tablica_indexów[index_z_tab_index] < N:
                lista_tymczasowa_do_wyboru.append(tablica[wiersz][tablica_indexów[index_z_tab_index]])


        najw_liiczba,jej_index = njamniejsza_liczba_z_tablicy(lista_tymczasowa_do_wyboru)
        if najw_liiczba not in posortowana_lista_jedna:
            posortowana_lista_jedna.append(najw_liiczba)

        while True:
            if tablica_indexów[jej_index] < N:
                tablica_indexów[jej_index] += 1
                break
            jej_index +=1



    print(tablica)
    for bruh in tablica:
        print(bruh)


    print(posortowana_lista_jedna)

    return tablica

przepisywanie_sigletony(4)

