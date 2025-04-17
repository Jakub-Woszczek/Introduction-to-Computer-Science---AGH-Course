import time

liczba = str(input('Podaj liczbę do sprawdzenia: '))
liczba = liczba.replace(" ","")
print(liczba)
licz_pier = int(liczba)

def is_prime_v1(a):
    i = 2

    while i <= a**(1/2):
        if licz_pier % i == 0:
            return False
        i +=1
    return True
start1 = time.time()
for i in range(1,licz_pier):
    print(is_prime_v1(i))

end1 = time.time()
def is_prime_v2(a):
    i = 3

    if a%2 == 0:
        return False
    while i <= a**(1/2):
        if licz_pier % i == 0:
            return False
        i +=2
    return True
start2 = time.time()
for i in range(1,licz_pier):
    print(is_prime_v2(i))
end2 = time.time()

def is_prime_v3(a):
    i = 5
    if a % 2 ==0 or a % 3 == 0:
        return False

    while i <= a**(1/2):
        if licz_pier % i == 0:
            return False
        i += 2
        if licz_pier % i == 0:
            return False
        i += 4
    return True

for i in range(1,licz_pier):
    print(is_prime_v3(i))



czas_cał1 = end1 - start1
czas_cał2 = end2 - start2
czas_cał3 = end3 - start3
print(czas_cał1,'\n',czas_cał2,'\n',czas_cał3)