import math

def liczby_pierwsze_do_N(N):
    lista_pierwszych = []
    lista_T_F = [True for _ in range(N+1)]
    lista_T_F[0] = False
    lista_T_F[1] = False
    for i in range(2,int(math.sqrt(N))+1):
        if lista_T_F[i] == True:
            for k in range(i*i,N+1,i):
                lista_T_F[k] = False


    for i in range(len(lista_T_F)):
        if lista_T_F[i] == True:
            lista_pierwszych.append(i)


    return lista_pierwszych

N = int(input('Podaj N: '))
lista_pierwszych =liczby_pierwsze_do_N(N)
print(lista_pierwszych, '\nilość = ', len(lista_pierwszych))
