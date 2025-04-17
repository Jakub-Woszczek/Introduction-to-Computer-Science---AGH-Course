x = int(input('Podaj liczbę:'))
root = int(x**(1/2))
nr_elem = 0
m = None
lista_podz = []
for i in range (2,root+1):
    if x % i ==0:
        m = int(x/i)
        lista_podz.append(i)
        lista_podz.append(m)




    i += 1
lista_podz.sort()
print(lista_podz)