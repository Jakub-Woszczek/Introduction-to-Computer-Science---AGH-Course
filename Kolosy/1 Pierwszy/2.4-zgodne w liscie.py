def na_sys_4(num):
    liczba = 0
    mnożenie = 0
    while num !=0:
        cyfra = num%4
        num//=4
        liczba += cyfra*(10**mnożenie)
        mnożenie +=1

    return liczba

print(na_sys_4(123))

def lista_cyfr(num):
    lista = [1 if i == 0 else 0 for i in range(10)]

    while num !=0:
        cyfra = num%10
        lista[cyfra] = cyfra
        num //=10

    return lista

print(lista_cyfr(12450))