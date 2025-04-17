def czy_w_liście_każda_liczba_ma_cyfra_pierwsza(list):
    pierwsze = [2,3,5,7]

    for index in list:
        while index != 0:
            cyfra = index%10
            if cyfra in pierwsze:
                break
            index //=10

        if index == 0:
            return False
    print(f'lista {list}')
    return True

def czy_każdy_wiersz(N):
    import random
    T = [[random.randint(2,100) for _ in range(N)] for _ in range(N)]

    for mech in T:
        print(mech)

    for bruh in T:
        if czy_w_liście_każda_liczba_ma_cyfra_pierwsza(bruh) == True:
            return True
    return False


# print(czy_każdy_wiersz(5))
print(czy_w_liście_każda_liczba_ma_cyfra_pierwsza([35, 15, 82, 82, 47]))