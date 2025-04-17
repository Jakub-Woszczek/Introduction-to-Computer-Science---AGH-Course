def pierwiastek_kw(liczba):
    a = liczba
    b = 1
    srednia = 0
    EPS = 1e-8
    while abs(a - b) > EPS:
        srednia = (a+b)/2
        a = srednia
        b = liczba/srednia
    return (a)

def pierwiastek_sze(liczba):
    a = liczba
    b = 1
    c = 1
    srednia = 0
    EPS = 1e-6
    while abs(a-b)>EPS:
        srednia = (a + b + c)/3
        a= srednia
        b = pierwiastek_kw(liczba/srednia)
        c = b


    return (a)

x = int(input("Podaj ilczbe: "))
test = pierwiastek_sze(x)
print(test)


