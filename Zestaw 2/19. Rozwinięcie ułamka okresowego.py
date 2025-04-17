def ułamek_bez_całkowitych(a,b):
    dzielenie = a/b

    rozw_dziesientne = dzielenie-int(dzielenie)

    p = 1

    #while p<20:



    return rozw_dziesientne


def szukanie_okresu(a,b):

    for i in range(1,8):
        pierwszy_okres = int((ułamek_bez_całkowitych(a,b))*(10**i))
        print('pier okr', pierwszy_okres)
        dziesiętna = (ułamek_bez_całkowitych(a,b)*(10**(2*i)))
        print('dzies',dziesiętna)
        ilośc_całośći_dzies = (dziesiętna//10**i)*10**i
        print("ilosć cal",ilośc_całośći_dzies)
        drugi_okres = int(dziesiętna - ilośc_całośći_dzies)
        print("dr z dzies",drugi_okres)




        if pierwszy_okres == drugi_okres:
            ułamek_z_nawiasem = f'{int(a/b)}.({drugi_okres})'

            return ułamek_z_nawiasem


print(szukanie_okresu(1,7))


