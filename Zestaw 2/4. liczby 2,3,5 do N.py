N = int(input('Podaj liczbę do której mam sprawdzić: '))
liczba = 0
for m in range (1,N+1):
    i=m
    while i%2 ==0:
        i=i/2
    while i%3 ==0:
        i=i/3
    while i%5 ==0:
        i=i/5
    if i == 1:
        liczba +=1
        if m ==N:
            print(m)
        else:
            print(m, end=",")

    i +=1

print("\nJest ich: ",liczba)