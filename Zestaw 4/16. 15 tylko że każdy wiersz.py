def czy_w_liście_każda_liczba_ma_cyfra_pierwsza(list):
    pierwsze = [2,3,5,7]

    for index in list:
        iterator = 0
        count = 0
        while index != 0:
            cyfra = index%10
            if cyfra in pierwsze:
                count+=1
            iterator +=1
            index //=10

        if iterator == count:
            print(f'lista {list}')
            return True

    return False

def czy_każdy_wiersz(N):
    import random
    T = [[random.randint(2,100) for _ in range(N)] for _ in range(N)]

    for mech in T:
        print(mech)

    count = 0
    for bruh in T:
        if czy_w_liście_każda_liczba_ma_cyfra_pierwsza(bruh) == True:
            count +=1
    if count == N:
        return True
    return False


print(czy_każdy_wiersz(5))
# print(czy_w_liście_każda_liczba_ma_cyfra_pierwsza([35, 15, 82, 82, 47]))
tablica =czy_każdy_wiersz(3)
while tablica != True:
    print(tablica)
    tablica = czy_każdy_wiersz(3)
print(tablica)