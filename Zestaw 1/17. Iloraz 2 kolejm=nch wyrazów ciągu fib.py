
max = 0
def ciąg_fib(wyraz_1,wyraz_2,max_literacja):
    a = wyraz_1
    b = wyraz_2
    i = 0
    max = max_literacja
    sum = wyraz_1 + wyraz_2
    while max>i:

        a = b
        b = sum
        sum = a + b
        i += 1
    return max
ciąg_fib(1,1,50)
print(max)


#######################################


def fib_z_iloczynem(liczba1,liczba2):
    a = liczba1
    b = liczba2
    i=0
    suma_prev = a +b
    while i<100:
        a = b
        b = suma_prev
        suma_prev = a + b
        i +=1
    iloczyn = float(suma_prev/b)
    return iloczyn

for x in range(1,11):
    for y in range(1,11):
        iloczyn = fib_z_iloczynem(x,y)
        print(f'Dla liczb początkowych: {x},{y} ciąg zmierza do {iloczyn}')



