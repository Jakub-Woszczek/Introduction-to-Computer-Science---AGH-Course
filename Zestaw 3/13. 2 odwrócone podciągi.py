import random

def szukanie_reversed_podciagów(N):
    tablica = [101, 100, 100, 102, 101, 102, 102, 100, 100, 101, 100, 101, 100, 101, 102, 102, 101, 102, 102, 100]
    # for _ in range(N):
    #     losowa = random.randint(100,102)
    #     tablica.append(losowa)

    max_cunt = 0
    st_index = 0
    last_index = len(tablica)-1
    a,b = 0,0
    i,j = 0,0
    podciąg = []
    max_pocion = []
    for _ in range(N-1):
        st_index +=1
        a += 1
        for _ in range(N-1):
            cunt = 1
            if tablica[st_index] == tablica[last_index] and (last_index-st_index) >1:
                while (st_index + i)<len(tablica) and (last_index-j)>=0 and    tablica[st_index+i] == tablica[last_index-j]:
                    j += 1
                    i += 1
                    b += 1
                    cunt +=1
                    podciąg.append(tablica[st_index+i])
                if cunt > max_cunt and st_index != (last_index-j):
                    max_cunt = cunt
                    max_pocion = podciąg.copy()

            last_index -=1


    return max_cunt,tablica,max_pocion

liczba,tablica,max = szukanie_reversed_podciagów(20)
print(liczba)
print(tablica)
print(max)