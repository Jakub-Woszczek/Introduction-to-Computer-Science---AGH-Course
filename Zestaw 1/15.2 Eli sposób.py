import math

def jeden_pierwiastek(a):
    liczba = math.sqrt(0.5)
    while a > 1:
        y = math.sqrt(liczba * 0.5 + 0.5)
        liczba = y
        a -= 1
    return liczba

print(jeden_pierwiastek(2))
iloczyn = 1
m = 1
for i in range(1,99):

    iloczyn = iloczyn*jeden_pierwiastek(i)

print(m)
pi = 2/iloczyn

print(f'Pi = {pi} Ezzzzz')