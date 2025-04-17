def na_trójkowy(num):
    i = 0
    bin = 0
    while num !=0:
        reszta = num % 3
        num //= 3

        bin += reszta*10**(i)
        i+= 1

    return bin

def czy_pierwsza(num):
    if num % 2 ==0 or num % 3 == 0 or num == 1:
        return False
    else:
        for i in range(2,num-2):
            if num%i == 0:
                return False
    return True

def kombinacje(t1,t2):
    suma_prime = 0
    lista_sum = []
    if len(t1)>len(t2):
        for i in range(len(t2),len(t1)):
            suma_prime += t1[i]
    else:
        for i in range(len(t1),len(t2)):
            suma_prime += t2[i]
    print(suma_prime)
    len_dłuższa = 0
    if len(t1)>len(t2):
        len_dłuższa = len(t2)
    else:
        len_dłuższa = len(t1)

    for num_trojka in range(3**(len_dłuższa-1),3**(len_dłuższa)):
        num_trojka=na_trójkowy(num_trojka)
        numer_tablicy = 0
        suma = suma_prime
        while num_trojka !=0:
            znacznik = num_trojka%10
            num_trojka //=10
            if znacznik == 0:
                suma += t1[numer_tablicy]
            elif znacznik == 1:
                suma += t2[numer_tablicy]
            else:
                suma += (t1[numer_tablicy] + t2[numer_tablicy])

            numer_tablicy +=1

        if czy_pierwsza(suma) == True:
            print(suma)
            if suma not in lista_sum:
                lista_sum.append(suma)



    return lista_sum



t1 = [1,3,2,4,1,2]
t2 = [9,7,4,8]

print(kombinacje(t1,t2))