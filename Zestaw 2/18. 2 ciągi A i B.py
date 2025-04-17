def wartość_A(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        A = wartość_A(n-1) - wartość_B(n-1)*wartość_A(n-2)
        return A

def wartość_B(n):
    if n == 0:
        return 2
    else:
        B = wartość_B(n-1) + 2*wartość_A(n-1)
        return B


for i in range(1,20):
    print(wartość_A(i),wartość_B(i))
