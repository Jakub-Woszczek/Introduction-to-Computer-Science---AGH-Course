def czy_pierwsza(num):
    if num % 2 ==0 or num % 3 == 0 or num == 1:
        return False
    else:
        for i in range(2,num-2):
            if num%i == 0:
                return False
    return True

def czy_złożona(num):
    import math
    a = num
    for i in range(2,int(math.sqrt(num))+1):
        while num % i == 0:
            num /= i
            num = num/(a/i)
    if num == 1:
        return True
    else:
        return False

def czy_w_tablicy_indexy_fib_złożone(N):
    import random
    tablica = []
    for _ in range(N):
        liczba = random.randint(1,N)
        tablica.append(liczba)

    a = 1
    iterator = 0
    czy_jest = 0
    b = 1
    tablica_fib = []
    while a<(N-1):

        if iterator !=a and czy_jest != 1:
            czy_jest +=1

        if czy_złożona(tablica[a]) == True:
            tablica_fib.append(tablica[a])
            print(a,b,tablica[a])

        else:
            return False,tablica
        a,b = b,a+b

    if czy_jest == 1:
        return True, tablica
    else:
        return False





print(czy_w_tablicy_indexy_fib_złożone(20))