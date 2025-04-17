def współczynnik_k(tablica):
    import math

    bok = int(math.sqrt(len(tablica)))
    iloczyn_1 = bok-1
    iloczyn_2 = len(tablica)-bok
    k = tablica[0]*tablica[len(tablica)-1]*tablica[iloczyn_1]*tablica[iloczyn_2]

    return k

def szukanie_środka(T,k):
    T =[[23, 6, 18, 54, 2], [6, 18, 54, 162, 486], [2, 54, 2, 486, 1458], [54, 162, 486, 1458, 4374], [2, 486, 2, 4374, 2]]

    długość_boku = 3
    for _ in range((len(T)-3)//2+1):
        dł_przemieszczenia = len(T)-długość_boku+1
        for wiersz in range(dł_przemieszczenia):
            for kolumna in range(dł_przemieszczenia):
                tablica_tymczasowa = []
                for wsp_1 in range(długość_boku):
                    for wsp_2 in range(długość_boku):
                        tablica_tymczasowa.append(T[wiersz+wsp_1][kolumna+wsp_2])
                if współczynnik_k(tablica_tymczasowa) == k:
                    współżędne = [długość_boku // 2 + wiersz, długość_boku // 2 + kolumna]
                    return współżędne
        długość_boku +=2

    return False

print(szukanie_środka(2,16))

