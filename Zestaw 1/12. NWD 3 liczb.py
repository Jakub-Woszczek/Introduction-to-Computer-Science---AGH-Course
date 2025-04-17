def dzielniki_liczby(liczba):
    lista_podz = [1,liczba]
    root = int(liczba ** (1 / 2)) + 1
    for i in range(2, root):
        if liczba % i == 0:
            lista_podz.append(i)
            lista_podz.append(int(liczba/i))
            if i == int(liczba / i):
                lista_podz.remove(i)
        lista_podz.sort()
    return lista_podz

#print(dzielniki_liczby(12))
a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
c = int(input('Podaj trzecią liczbę: '))
#def NWD_3_liczb(a,b,c):
lista_1 = dzielniki_liczby(a)
lista_2 = dzielniki_liczby(b)
lista_3 = dzielniki_liczby(c)
print(lista_1)
print(lista_2)
print(lista_3)
wspolne_el = list(set(lista_1) & set(lista_3) & set(lista_2))
print(wspolne_el[-1])