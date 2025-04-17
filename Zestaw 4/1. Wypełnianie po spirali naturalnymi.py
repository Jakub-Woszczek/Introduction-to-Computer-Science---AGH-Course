#tablica [ wiersz ] [ kolumna ]

def spirala_naturalnych(długość_boku):

    if długość_boku%2 == 1:
        rozmiar = długość_boku
        tablica_dwuwymiarowa = [[0 for _ in range(rozmiar)] for _ in range(rozmiar)]

        współżędne_początku = int(długość_boku//2)
        kolumna = współżędne_początku
        wiersz = współżędne_początku
        print(wiersz)
        print(kolumna)

        tablica_dwuwymiarowa[wiersz][kolumna] = 1 # 2,2
        naturalna = 2

        iterator = 2
        for _ in range(długość_boku//2):

            for bruh in tablica_dwuwymiarowa:
                print(bruh)
            print("\n")

            # -> jeden
            kolumna +=1
            print(wiersz)
            print(kolumna)
            tablica_dwuwymiarowa[wiersz][kolumna] = naturalna # 2,3
            naturalna +=1
            # | góra
            for _ in range(iterator-1):
                wiersz -= 1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna  # 1,3
                naturalna += 1

            for bruh in tablica_dwuwymiarowa:
                print(bruh)
            print("\n")

            for _ in range(iterator):
                # <- w prawo
                kolumna -= 1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
                naturalna +=1

            for bruh in tablica_dwuwymiarowa:
                print(bruh)
            print("\n")

            for _ in range(iterator):
                # | w dół
                wiersz += 1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
                naturalna +=1

            for bruh in tablica_dwuwymiarowa:
                print(bruh)
            print("\n")

            for _ in range(iterator):
                # w lewo ->
                kolumna += 1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
                naturalna +=1

            for bruh in tablica_dwuwymiarowa:
                print(bruh)
            print("\n")

            iterator +=2

        for bruh in tablica_dwuwymiarowa:
            print(bruh)
        print("\n")

    if długość_boku % 2 == 0:
        rozmiar = długość_boku
        tablica_dwuwymiarowa = [[0 for _ in range(rozmiar)] for _ in range(rozmiar)]

        naturalna = 1
        wiersz = int(długość_boku/2)
        kolumna = int(długość_boku/2)
        print(wiersz)
        print(kolumna)


        iterator_v2 = 0
        for _ in range(int(długość_boku/2)):

            kolumna -=1
            tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
            naturalna +=1

            for _ in range(iterator_v2):
                wiersz +=1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
                naturalna += 1

            iterator_v2 +=1

            for _ in range(iterator_v2):
                kolumna +=1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
                naturalna += 1

            for _ in range(iterator_v2):
                wiersz -= 1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
                naturalna += 1

            for _ in range(iterator_v2):
                kolumna -=1
                tablica_dwuwymiarowa[wiersz][kolumna] = naturalna
                naturalna += 1

            iterator_v2 +=1




    return tablica_dwuwymiarowa

tablica = spirala_naturalnych(4)

column_width = 4

for row in tablica:
    print(" ".join(f"{num:>{column_width}}" for num in row))