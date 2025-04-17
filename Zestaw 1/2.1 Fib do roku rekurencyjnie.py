import time
rok = int(input('podaj rok: '))
start = time.time()
def fib_roku_o_najmniejszej_sum(rok):
    min_suma = rok

    for a in range(rok//2,rok):
        b = rok

        while a-(b-a)>0:

            a,b = b-a,a
        if a + b != rok:
            suma = a +b
            if suma < min_suma:
                min_suma = suma
                pocz1 = a
                pocz2 = b

    print(min_suma, )
    print(f'pocz1: {pocz1}, pocz2: {pocz2}')

fib_roku_o_najmniejszej_sum(rok)


end = time.time()

time = end-start
print(time)