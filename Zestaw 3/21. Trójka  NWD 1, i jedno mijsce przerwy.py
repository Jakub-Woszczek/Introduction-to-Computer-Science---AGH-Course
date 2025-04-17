def czy_1_to_NWD(num1,num2,num3):
    dzielnik = 2
    lista_1 = []
    lista_2 = []
    lista_3 = []
    while num1 != 1:
        if num1 % dzielnik == 0:
            lista_1.append(dzielnik)
            num1 /=dzielnik
            dzielnik = 1

        dzielnik += 1
    while num2 != 1:
        if num2 % dzielnik == 0:
            lista_2.append(dzielnik)
            num2 /= dzielnik
            dzielnik = 1

        dzielnik += 1
    while num3 != 1:
        if num3 % dzielnik == 0:
            lista_3.append(dzielnik)
            num3 /= dzielnik
            dzielnik = 1

        dzielnik += 1



    for i in range(len(lista_1)):
        if lista_1[i] in lista_2 and lista_1[i] in lista_3:
            return False
    return True

def trójki(T):
    liczba_trójek = 0
    lista_trójek = []
    for index_1 in range(len(T)-2):
        index_2 = index_1 +1
        index_3 = index_2 +1

        if czy_1_to_NWD(T[index_1],T[index_2],T[index_3]) == True:
            trójka = [T[index_1],T[index_2],T[index_3]]
            lista_trójek.append(trójka)
            liczba_trójek +=1

    for index_1 in range(len(T) - 3):
        index_2 = index_1 + 1
        index_3 = index_2 + 2

        if czy_1_to_NWD(T[index_1], T[index_2], T[index_3]) == True:
            trójka = [T[index_1], T[index_2], T[index_3]]
            lista_trójek.append(trójka)
            liczba_trójek += 1


    for index_1 in range(len(T) - 3):
        index_2 = index_1 + 2
        index_3 = index_2 + 1

        if czy_1_to_NWD(T[index_1], T[index_2], T[index_3]) == True:
            trójka = [T[index_1], T[index_2], T[index_3]]
            lista_trójek.append(trójka)
            liczba_trójek += 1

    for index_1 in range(len(T) - 4):
        index_2 = index_1 + 2
        index_3 = index_2 + 2

        if czy_1_to_NWD(T[index_1], T[index_2], T[index_3]) == True:
            trójka = [T[index_1], T[index_2], T[index_3]]
            lista_trójek.append(trójka)
            liczba_trójek += 1


    return liczba_trójek,lista_trójek



def generator_tablicy(długość):
    import random
    tablica = []
    for i in range(długość):
        liczba = random.randint(1,100)
        tablica.append(liczba)

    return tablica

tablica = generator_tablicy(100)

print(trójki([7,8,5,3,17]))

