def przelicz_na_system(num,s):
    result = ''

    while num != 0:
        next_digit = num % s
        num //= s
        # if next_digit >= 10:
        #     next_digit -=10
        #     result = chr(ord("A") + next_digit) + result
        # else:
        result = str(next_digit) + result

        # print(str(next_digit))

    return int(result)

def ile_jedynek(num):

    ilość = 0

    while num != 0:
        if num%2 == 1:
            ilość += 1
        num //= 10

    return ilość


def dłusość_całkowita(a,b):
    ilość_cyfr = 0

    while a != 0:
        a //=10
        ilość_cyfr +=1
    while b != 0:
        b //=10
        ilość_cyfr +=1

    return ilość_cyfr

def kombinator_a_b(a,b):


    długość_a = dłusość_całkowita(a,0)
    długość_b = dłusość_całkowita(0,b)
    ostatnia = dłusość_całkowita(a,b)
    max_maska_dec = 2**(ostatnia)
    lista_result = []

    for i in range(1,max_maska_dec):
        p = 0
        result = 0
        maska = przelicz_na_system(i,2)


        if ile_jedynek(maska) == długość_a:
            #print(i,maska)
            a1 = a
            b1 = b
            while a1 != 0 or b1 != 0 :
                d = maska%2
                maska //=10
                if d == 1:
                    result += (a1%10)*(10**p)
                    a1 //= 10
                else:
                    result += (b1%10)*(10**p)
                    b1 //= 10

                p += 1
            lista_result.append(result)


    return lista_result

#print(kombinator_a_b(123,75))



def is_prime_v1(a):
    i = 2

    while i <= a**(1/2):
        if a % i == 0:
            return False

        i +=1
    return True


lista_kombinacji = kombinator_a_b(96,3907)

print(lista_kombinacji)
for i in range (0,len(lista_kombinacji)):
    if is_prime_v1(lista_kombinacji[i]) == True:
        print(lista_kombinacji[i])