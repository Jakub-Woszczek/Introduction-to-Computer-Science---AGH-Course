a = int(input('a= '))
b = int(input('b= '))

def EUKLIDES_1(a,b):
    while a!=b:
        if a>b:
            a -=b
        else:
            b-=a
    if a == 1 or b ==1:
        a = "liczby nie mają NWD"
        b = None
        return (a)
    else:
        return (a)

def EUKLIDES_2(a,b):
    while b:
        a,b = b,a%b
        print(a,b)
    return (a)

    

print('z 1: ',EUKLIDES_1(a,b))
print('z 2: ',EUKLIDES_2(a,b))
print(3/2)
print(5//2)
print(5%2)