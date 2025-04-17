def ile_liczba_ma_cyfr(num):
    ilość = 0
    while num !=0:
        num //=10
        ilość +=1

    return ilość

def czy_zawiera_cyfre_ilości(num):
    ilość_cyfr = ile_liczba_ma_cyfr(num)
    a = ilość_cyfr
    if ilość_cyfr>=10:
        return False
    else:
        while a != 0:
            cyfra_1 = num % 10
            if cyfra_1 == ilość_cyfr:
                return True
            else:
                a -=1
                num //=10
        return False

print(czy_zawiera_cyfre_ilości(12346))
