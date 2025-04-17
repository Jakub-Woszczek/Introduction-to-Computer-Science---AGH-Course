a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
n = int(input('Podaj ile miejsc po przecinku: '))
i = 0
next_reszta = 0
print(a // b, end=',')
while i < n:

    reszta = ((a % b)*10)//b
    a = (a%b)*10
    next_reszta = ((a - (reszta*b))*10)//b
    if i+1==n and next_reszta>=5:
        reszta +=1

    print(reszta, end="")
    i += 1
