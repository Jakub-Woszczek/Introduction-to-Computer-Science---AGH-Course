import math

def porównanie_list_są_te_same(t1,t2):
    for i in range(len(t1)):
        for j in range(len(t2)):
            if t1[i] == t2[j]:
                return True
    return False

def czynniki_pierwsze(num):
    lista_czynników = []
    cpy = num
    if num == 2:
        return [2]
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:

            lista_czynników.append(i)
            if math.sqrt(num) != i:
                lista_czynników.append(int(num / i))
            num //= i
            num //=(cpy/i)

            if num%i ==0:
                return False
    if num !=1:
        lista_czynników.append(num)
    return lista_czynników

def podciąg_jeden_czynnik(T):
    max_cunt = 0
    for index in range(len(T)-1):
        cunt = 1

        if czynniki_pierwsze(T[index]) !=False:
            lista_czynników = czynniki_pierwsze(T[index])

            iterator = index+1

            while iterator<len(T) and czynniki_pierwsze(T[iterator]) != False and porównanie_list_są_te_same(lista_czynników,czynniki_pierwsze(T[iterator])) ==False:
                lista_czynników += czynniki_pierwsze(T[iterator])
                cunt +=1
                iterator +=1

            if cunt>max_cunt:
                max_cunt = cunt


    return max_cunt




print(podciąg_jeden_czynnik([2,23,33,35,7,4,6,7,5,11,13,22]))