root = float(input('Podaj liczbe do spierwiastkowania: '))
a = float(1)
pole = a*root
print(a)
i = 0
b = root
while i <1000000:
    srednia = (a + b)/2
    a = srednia
    b = pole/srednia
    i +=1
    if a - b < 0.0001:
        break
print(a)
print(b)

