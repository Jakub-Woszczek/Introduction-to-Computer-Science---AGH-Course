import time
rok = int(input('podaj rok: '))
start = time.time()
def suma_najmniejsza_fib_do_danej_lilczby(a):
    najmniejsza_początkowa1 = 0
    najmniejsza_początkowa2 = 0
    a= rok
    sum = 0
    najmniejsza_suma = rok
    for x in range(1, rok + 1):
        for y in range(1, x + 1):
            a, b = x, y
            while a + b < rok:
                a, b = a + b, a
                if a + b == rok:
                    sum = x + y
                    if sum < najmniejsza_suma:
                        najmniejsza_suma = sum
                        najmniejsza_początkowa1 = x
                        najmniejsza_początkowa2 = y
                        print(x,y)

    return (najmniejsza_suma,najmniejsza_początkowa1,najmniejsza_początkowa2)

suma_najmniejsza_fib_do_danej_lilczby(rok)



end = time.time()

time = end-start
print(time)


