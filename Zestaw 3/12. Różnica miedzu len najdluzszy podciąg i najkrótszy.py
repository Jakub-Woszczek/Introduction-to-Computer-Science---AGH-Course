import random

def kopia_listy(lista):
    lista_kopia = []
    for element in lista:
        lista_kopia.append(element)
    return lista_kopia

def najdłuższy_spójny_podciąg_o_tej_samej_różnicy_dodatniej(tablica):
    różnica = 0
    lista_podciągów = []
    max_podciąg = []
    a = 0
    b = 1
    długość = 0
    lista = []

    for i in range(len(tablica)-1):

        if tablica[a] < tablica[b] and len(lista)==0:
            różnica = tablica[b] - tablica[a]

        if tablica[a] < tablica[b] and tablica[b] - tablica[a] == różnica:

            if tablica[a] not in lista:
                lista.append(tablica[a])
            lista.append(tablica[b])
            długość += 1

        if tablica[a] >= tablica[b]:

            if len(lista)>(len(max_podciąg)-1) and różnica>0:
                max_podciąg = kopia_listy(lista)
                max_podciąg.append(różnica)

            lista.clear()
            # lista.append(tablica[a])

        a += 1
        b += 1
    różnica = max_podciąg[len(max_podciąg)-1]
    max_podciąg.pop(len(max_podciąg)-1)
    return max_podciąg


def najdłuższy_spójny_podciąg_o_tej_samej_różnicy_ujmenej(tablica):
    różnica = 0
    lista_podciągów = []
    max_podciąg = []
    a = 0
    b = 1
    długość = 0
    lista = []

    for i in range(len(tablica)-1):

        if tablica[a] > tablica[b] and len(lista)==0:
            różnica = tablica[b] - tablica[a]

        if tablica[a] > tablica[b] and tablica[b] - tablica[a] == różnica:

            if tablica[a] not in lista:
                lista.append(tablica[a])
            lista.append(tablica[b])
            długość += 1

        if tablica[a] <= tablica[b]:

            if len(lista)>(len(max_podciąg)-1) and różnica<0:
                max_podciąg = kopia_listy(lista)
                max_podciąg.append(różnica)

            lista.clear()
            # lista.append(tablica[a])

        a += 1
        b += 1
    różnica = max_podciąg[len(max_podciąg)-1]
    max_podciąg.pop(len(max_podciąg)-1)
    return max_podciąg


def różnica_między_długościamy_pythongów(N):
    różnica = None
    tablica = []
    for i in range(N):
        liczba_randomowa = random.randint(1,99)
        tablica.append(liczba_randomowa)

    ciąg_dodatni = najdłuższy_spójny_podciąg_o_tej_samej_różnicy_dodatniej(tablica)
    ciąg_ujemy = najdłuższy_spójny_podciąg_o_tej_samej_różnicy_ujmenej(tablica)
    różnica = abs(len(ciąg_ujemy)-len(ciąg_dodatni))
    return różnica,ciąg_dodatni,ciąg_ujemy

def różnica_między_długościamy_pythongów_tablica(tablica):
    różnica = None
    # tablica = []

    ciąg_dodatni = najdłuższy_spójny_podciąg_o_tej_samej_różnicy_dodatniej(tablica)
    ciąg_ujemy = najdłuższy_spójny_podciąg_o_tej_samej_różnicy_ujmenej(tablica)
    różnica = abs(len(ciąg_ujemy)-len(ciąg_dodatni))
    return różnica,ciąg_dodatni,ciąg_ujemy


print(różnica_między_długościamy_pythongów(10000))

print(różnica_między_długościamy_pythongów_tablica([1,2,3,4,3,6,9,12,15,7,-1,8,9,4,5]))


