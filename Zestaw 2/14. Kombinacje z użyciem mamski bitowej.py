def ile_jedynek_w_sys_binarnym(num):
    cnt = 0

    while num != 0:
        cnt += num % 2
        num //=2

    return cnt

def ilość_cyfr(num):
    cnt = 0
    while num !=0:
        cnt +=1
        num //=10

    return cnt

def złączenie_liczb(a,b,m):
    result = 0
    p = 0
    m //=2
    while a != 0 and b != 0:
        d = m % 2

        if d == 1:
            result += (a%10)*(10**p)
            a //=10

        else:
            result += (b % 10) * (10 ** p)
            b //= 10

    return result + (a % (10 ** p)) + (b * (10**p))


def ile_liczb_pierwszych(a,b):

    ilość_jednynek = ile_jedynek_w_sys_binarnym(a)
    długość_maski = ilość_cyfr(b) + ilość_jednynek

    max_maska = 2 ** (długość_maski + 1 )

    cnt = 0

    for m in range(1,max_maska):
        if ilość_jednynek == ile_jedynek_w_sys_binarnym(m):
            print(złączenie_liczb(a,b,m))
            if (is_prime_v3(złączenie_liczb(a,b,m))):
                cnt += 1

    return cnt

def is_prime_v3(a):
    #liczba = str(input('Podaj liczbę do sprawdzenia: '))
    #liczba = liczba.replace(" ", "")
    #rint(liczba)
    a = int(a)
    i = 5
    if a % 2 ==0 or a % 3 == 0:
        return False

    while i <= a**(1/2):
        if a % i == 0:
            return False
        i += 2
        if a % i == 0:
            return False
        i += 4
    return True



ile_liczb_pierwszych(123,75)

print(złączenie_liczb(123,57,2))