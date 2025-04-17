import math
srodek_dodawanie = 0
y = ((0.5)*math.sqrt(0.5))
pier_kon = 0.5*math.sqrt(0.5)
print('y', y)
def krotnosci_srodek(a):

    if a ==1:
        srodek_dodawanie = 0.5 * math.sqrt(0.5 + krotnosci_srodek(a - 1))

    else:
        return  y

    #srodek_dodawanie = math.sqrt(srodek_dodawanie) * math.sqrt(0.5)

    return srodek_dodawanie

for a in range(2,20):
    x = krotnosci_srodek(a)*math.sqrt(0.5)
    pi = 2 / (x)
    print(x, pi)

