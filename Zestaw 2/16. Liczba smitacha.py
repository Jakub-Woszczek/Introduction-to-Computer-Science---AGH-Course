def len_cyfry(num):
    ilość_cyfr = 0

    while num != 0:
        num //= 10
        ilość_cyfr += 1

    return ilość_cyfr


def suma_cyfr(num):
    długość = len_cyfry(num)
    suma_całkowita = 0
    for m in range (1,długość+1):
        d = m%10
        suma_całkowita += d
        m //=10
    suma_całkowita +=m

    return suma_całkowita




def czy_liczba_smitcha(num):
    suma = 0

    while num != 1:
        i = 2
        sprawdzam = 2
        while sprawdzam != 1:
            if num % i == 0:
                suma += suma_cyfr(i)
                sprawdzam = 1
                print(i)
                num //=i
            i +=1

    return suma

print(czy_liczba_smitcha(12))






