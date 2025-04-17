lista_wartości = []
lista_10_wartości = []
n = 1
numer = 1
i = 0
pierwszy = 0
ilość_liczb = 0
while n != 0:

    while n != 0:
        liczba = int(input(f"podaj liczbę nr.{numer} :"))
        numer += 1

        if pierwszy == 0:
            lista_wartości.append(liczba)
            pierwszy = 1

        i = 0
        która_z_kolei = 0
        if liczba not in lista_wartości:
            while ilość_liczb >=i and lista_wartości[i] < liczba:
                i += 1
            lista_wartości.insert(i,liczba)
            ilość_liczb += 1
            if ilość_liczb>9:
                lista_wartości.pop(0)
                ilość_liczb -=1


        if liczba == 0:
            n = 0
            if 0 in lista_wartości:
                lista_wartości.remove(liczba)






print(lista_wartości)