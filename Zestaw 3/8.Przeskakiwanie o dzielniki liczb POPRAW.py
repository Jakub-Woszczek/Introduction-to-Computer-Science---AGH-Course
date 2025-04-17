import random

def rokład_na_czynnikki_pierwsze_pierwsze(num):
    tablica_pier_dzielnikow = []
    i = 2
    while num != 1:

        while num%i == 0:
            if i not in tablica_pier_dzielnikow:
                tablica_pier_dzielnikow.append(i)

            num //=i

        i += 1
    return tablica_pier_dzielnikow

tablica_t = []
N = int(input('Podaj długość tablicy: '))
for i in range(N):
    randomowa = random.randint(1, 100)
    tablica_t.append(randomowa)


def f(t,n=0):
    element = t[n]
    pierwsze = rokład_na_czynnikki_pierwsze_pierwsze(element)
    print(n)
    print(f'podzielniki n({element}): {rokład_na_czynnikki_pierwsze_pierwsze(element)}')

    for i in range (len(pierwsze)):
        if n + pierwsze[i] == len(t)-1:

            return True
        elif n + pierwsze[i] > len(t):
            return False

        else:
            if f(t,n+pierwsze[i]):

                return True





print(f(tablica_t,0))
print(tablica_t)