def czy_liczba_ma_cyfry_rosnące(num):
    pierwsza_cyfra = num % 10
    num //= 10
    druga_cyfra = num % 10
    num //= 10
    while num>1:


        if druga_cyfra<pierwsza_cyfra:
            pierwsza_cyfra = druga_cyfra
            druga_cyfra = num % 10
            num //= 10
        else:
            return False


    return True

print(czy_liczba_ma_cyfry_rosnące(123498))