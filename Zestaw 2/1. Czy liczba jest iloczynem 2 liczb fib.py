import time
import math
def ciag_fib_konkretna_liczba(a):

    liczba_pwtóżeń = a
    num1 = 1
    num2 = 1
    sum = 0
    i=2
    if liczba_pwtóżeń == 1 or liczba_pwtóżeń == 2:
        return 1

    while liczba_pwtóżeń > i:
        sum = num1 + num2
        num1 = num2
        num2 = sum
        liczba_pwtóżeń -= 1



    return sum





#iloczyn = 1
#pierwsza = 1
#druga = 1


def sprawdzenie_czy_iloczyn(dana_liczba):
    poszukiwany_iloczyn = dana_liczba
    powtorki = 2
    x = None
    y = None
    nie_ma = 'nie ma tekich liczb'

    while powtorki > 1:
        for x in range(1, int(liczba_naturalna/2)):
            for y in range(1, x+1):
                #print(x, y)
                pierwsza = ciag_fib_konkretna_liczba(x)
                druga = ciag_fib_konkretna_liczba(y)

                #print(pierwsza, druga)



                if liczba_naturalna == pierwsza * druga:
                    return pierwsza,druga

        powtorki -= 1
    if powtorki<2:
        return nie_ma



liczba_naturalna = int(input("podaj liczbę: "))
start= time.perf_counter()
print(sprawdzenie_czy_iloczyn(liczba_naturalna))

end = time.perf_counter()

print(end-start)