def rozszerzenie_tablicy(N):
    import random
    T = [[random.randint(1,9) for _ in range(N)] for _ in range(N)]

    for bruh in T:
        print(bruh)

    for iterator in range(N):
        T[iterator] = [0] + T[iterator] + [0]

    sufit = [[0 for _ in range(len(T)+2)]]
    podłoga = [[0 for _ in range(len(T)+2)]]

    T = sufit + T + podłoga

    return T





def sumy_sąsiadów(N):
    tablica = rozszerzenie_tablicy(N)
    max_sum = 0
    for row in range(1,len(tablica)-1):
        for column in range(1,len(tablica) - 1):
            sum = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if i != 0 or j != 0:
                        sum += tablica[row + i][column + j]



            if max_sum < sum:
                max_sum = sum
                coord = [row-1,column-1]

    return max_sum,coord

print(sumy_sąsiadów(4))