potenga = int(input('Podaj liczbę do spierwiastkowania: '))
a = 1
add = 2
ilość = 0
sum = 0
while sum<=potenga:
    sum += a
    a += add
    ilość += 1
print(ilość-1)