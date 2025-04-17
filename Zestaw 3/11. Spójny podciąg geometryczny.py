import random

def najdłuższy_podciąg_geo(N):
    tablica_cała = [None for _ in range(N)]
    for i in range(N):
        print(i)
        liczba = random.randint(1,10)
        random_multiple_of_3 = 3**liczba

        tablica_cała[i] = random_multiple_of_3
    # tablica_cała = [27,9,3,1,98,35,546,345]


    cunt_max = 0
    for index in range(len(tablica_cała)-2):
        podciąg_geo = []
        index_next = index+1

        count = 2
        q = tablica_cała[index]/tablica_cała[index_next]
        q_next = tablica_cała[index+1] / tablica_cała[index_next+1]
        a = index + 1
        b = index_next + 1
        podciąg_geo.append(tablica_cała[index])
        podciąg_geo.append(tablica_cała[index_next])
        while b<(N-1) and  q == q_next:




            q = q_next
            q_next = tablica_cała[a]/tablica_cała[b-1]

            a +=1
            b +=1
            podciąg_geo.append(tablica_cała[b-1])
            count +=1

        if count>cunt_max:
            cunt_max = count

            podciąg_max = podciąg_geo.copy()



    return cunt_max,tablica_cała,podciąg_max




print(najdłuższy_podciąg_geo(10))
