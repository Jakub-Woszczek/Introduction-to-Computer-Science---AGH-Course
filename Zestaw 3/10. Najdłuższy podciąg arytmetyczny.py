def kopia_listy(lista):
    lista_kopia = []
    for element in lista:
        lista_kopia.append(element)
    return lista_kopia




def najdłuższy_spójny_podciąg_o_tej_samej_różnicy(tablica):
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

            if len(lista)>len(max_podciąg):
                max_podciąg = kopia_listy(lista)

            lista.clear()
            # lista.append(tablica[a])

        a += 1
        b += 1
    return max_podciąg

print(najdłuższy_spójny_podciąg([1,2,3,4,3,6,9,12,15,7,8,9,4,5]))


################

def podciąg_rosnący(tablica):

    count = 1
    max_count = 0
    a = 1
    b = 0

    for i in range(len(tablica)-1):
        if tablica[a]>tablica[b]:
            count +=1
        elif tablica[a] <= tablica[b]:
            if count>max_count:

                max_count = count

            count = 1

        a += 1
        b += 1

    return max_count


print(podciąg_rosnący([1,2,3,4,3,6,7,8,8,9,4,5]))