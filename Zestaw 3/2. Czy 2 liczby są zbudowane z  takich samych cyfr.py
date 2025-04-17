def czy_2__liczby_z_takich_samych_cyfr(a,b):
    lista_cyfr = []


    while a !=0:
        digit = a%10
        if digit not in lista_cyfr:
            lista_cyfr.append(digit)
        a//=10

    while b !=0:
        digit = b%10
        if digit not in lista_cyfr:
            return False
        b//=10
    return True

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

print(czy_2__liczby_z_takich_samych_cyfr(a,b))
