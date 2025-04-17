n1 = 1
n2 = 1
suma = 0
sum = int(input('Podaj sumę: '))
lista_fib = []
while n1<sum:
    lista_fib.append(n1)
    suma = n1 + n2
    n1 = n2
    n2 = suma
wynik = 0
i = 0
print(lista_fib)
dlug = len(lista_fib) -1
for i in range(0, dlug):
    while wynik <= sum:
        y = lista_fib[i]
        i += 1
        wynik += y
        print(wynik)
        if wynik == sum:
            print(lista_fib[i])
###################################
for i in range(0, dlug):
    wynik=lista_fib[i]
    a=i
    while wynik < sum:
        a += 1
        wynik += lista_fib[a]
        # print(wynik)
    if wynik == sum:
        print(lista_fib[i],wynik)
