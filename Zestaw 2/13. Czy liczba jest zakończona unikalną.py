def czy_liczba_zakończona_inikalną(num):
    liczba_unikalna = num % 10
    num //=10
    while num != 0:
        next = num%10
        if next == liczba_unikalna:
            return False
        else:
            num //= 10
    return True

print(czy_liczba_zakończona_inikalną(4234))


