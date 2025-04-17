def max_2_5(mianownik):
    liczba_5 = 0
    liczba_2 = 0

    while mianownik % 2 == 0:
        liczba_2 +=1
        mianownik /=2

    while mianownik % 5 == 0:
        liczba_5 +=1
        mianownik /=5

    if liczba_2>liczba_5:
        return liczba_2
    else:
        return liczba_5

def ułam_okresowy(licznik,mianowanik):

    print(licznik//mianowanik, end='')
    licznik %= mianowanik

    if licznik != 0:
        print('.',end='')
        for _ in range(max_2_5(mianowanik)):
            licznik *= 10
            print(licznik//mianowanik,end='')

        licznik %= mianowanik

        licznik *= 10
        pierwszy_w_nawiasie = licznik//mianowanik
        drugi_w_nawiasie = (pierwszy_w_nawiasie*10)%mianowanik
        print('(',end='')


        while drugi_w_nawiasie != pierwszy_w_nawiasie:

            print(licznik//mianowanik, end='')
            licznik %=mianowanik
            drugi_w_nawiasie = (licznik*10)%mianowanik
            licznik *= 10

        print(licznik%mianowanik, end='')
        print(')',end='')


print(ułam_okresowy(1,7))
