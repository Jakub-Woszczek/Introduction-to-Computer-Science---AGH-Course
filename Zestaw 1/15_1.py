import math
y = (1/2)*math.sqrt(1/2)
def ciąg(a):
    if a>y:
        a = (0.5)+(0.5)*math.sqrt((0.5 + ciąg(a-1)))

        return a


    else:
        return y

x = ciąg(20)

print('pi=',2/(math.sqrt(0.5)*ciąg(100)))
