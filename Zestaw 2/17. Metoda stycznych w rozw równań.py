import math
X1 = 10
EPS = 1e-8

def rówanie(x):
    wartość = x**x - 2020
    return wartość

def pochodana_rrównania(x):
    wartość_pochodnej = x**x * (1 + math.log(x))
    return wartość_pochodnej

def x_2(x1):
    x2 = x1 - (rówanie(x1)/pochodana_rrównania(x1))
    return x2

def szukanie_Mz(X1):
    while rówanie(X1)>EPS:
        X1 = x_2(X1)

    return X1

print(szukanie_Mz(X1))





