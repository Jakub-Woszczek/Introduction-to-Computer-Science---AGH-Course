
def silnia(a):
     if a>1:
         a = a * silnia(a - 1)
     elif a == 0:
         a = 1

     return a

silnia(4)


sum = 0
for i in range (0, 1000):
    x = 1/silnia(i)
    sum += x

print(sum)










