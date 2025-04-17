# a<b<c

a = int(input('Podaj a='))
b = int(input('Podaj b='))
c = int(input('Podaj c='))
def NWD(a,b):
    while b !=0:
        a,b = b,a%b
    return (a)
def NWD3(a,b,c):
    return NWD(NWD(a,b),c)

print(NWD3(a,b,c))
