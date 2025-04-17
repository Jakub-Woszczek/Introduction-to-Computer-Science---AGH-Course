zadana_suma = int(input("podaj sumę: "))
sum = 0
n1 = 1
n2 = 1
suma_koncowa = 0
lista_sumy = []
while zadana_suma>suma_koncowa:
    lista_sumy.append(n1)
    suma_koncowa += n1
    sum = n1+n2
    n1 = n2
    n2 = sum


if suma_koncowa == zadana_suma:
    print('Tak ez:', lista_sumy)
else:
    n1 = 1
    n2 = 1
    sum = 0
    while zadana_suma < suma_koncowa:
        lista_sumy.remove(n1)
        suma_koncowa -= n1
        sum = n1 + n2
        n1 = n2
        n2 = sum


    if suma_koncowa == zadana_suma:
        print('Tak ez: ',lista_sumy)
    else:
        print('nie ma takiego ciągu bruh')

