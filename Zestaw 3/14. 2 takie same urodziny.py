import random

def prawdopodobieństwo_te_same_urodziny(N):
    ilość_wykonń = 1000
    cunt = 0
    for _ in range(ilość_wykonń):
        lista_dni = []
        for _ in range(N):
            dzień = random.randint(1,365)

            if dzień in lista_dni:
                cunt += 1
                break

            lista_dni.append(dzień)

    prawdopodobienstwo = cunt/ilość_wykonń

    return prawdopodobienstwo

lista_prawdopodobienstw = []
print(prawdopodobieństwo_te_same_urodziny(20))
for i in range(5,60):
    pr = prawdopodobieństwo_te_same_urodziny(i)
    lista_prawdopodobienstw.append(pr)

print(lista_prawdopodobienstw)
