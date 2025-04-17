EPS = 1e-8
import math
def ciągi(a,b):
    while abs(a-b)>EPS:
        a,b = math.sqrt(a * b), (a + b) / 2

    return a

for A in range(2,1001,100):
    for B in range(2,1001,100):
        A = ciągi(A,B)
        print(A)


print(ciągi(102,102))



