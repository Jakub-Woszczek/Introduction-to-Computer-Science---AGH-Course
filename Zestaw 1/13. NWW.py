a = int(input('a= '))
b = int(input('b= '))
import time
def NWW(a,b):


    x = a
    y = b

    while a != b:
        if a > b:
            b += y
        else:
            a += x
    return (a)

def NWD(a,b):
    while b !=0:
        a,b = b,a%b
    return (a)

def NWW_2(a,b):
    x = NWD(a,b)
    y = x*(int(a/x))*(int(b/x))
    return (y)

print(NWW(a,b))
print(NWW_2(a,b))




