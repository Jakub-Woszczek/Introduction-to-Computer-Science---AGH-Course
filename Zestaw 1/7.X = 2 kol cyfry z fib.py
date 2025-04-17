num_iloczyn = int(input('Podaj lioczyn 2 liczb fib: '))
n1= 1
n2 = 1
sum = None
while n1 <num_iloczyn:
    sum = n1 + n2
    n1 = n2
    n2 = sum

    print(n1,n2)
    if n1*n2 == num_iloczyn:
        print(f"Są liczby, pierwsza to {n1}, druga to {n2}")
        break
else:
    print('nie ma takich liczb')