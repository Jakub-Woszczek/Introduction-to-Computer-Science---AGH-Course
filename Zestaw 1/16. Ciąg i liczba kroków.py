LIM = 1
EPS = 1e-8
największa_kroków = 0
i = 0
def liczba_kroków(A):
    m = 0

    while abs(A-LIM)>EPS:
        A = (A % 2) * (A * 3 + 1) + (1 - (A % 2)) * A / 2
        m +=1
    return m

number = None
for i in range(2,10000+1):
    max_steps =0

    steps = liczba_kroków(i)

    if steps > największa_kroków:
        największa_kroków = steps
        number = i

print(największa_kroków,number)


