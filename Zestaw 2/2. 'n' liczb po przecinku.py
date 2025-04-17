def rozw_dzies_iloczynu_do_n(liczba):
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    n = int(input('Podaj ile miejsc po przecinku: '))
    iloczyn = a/b

    iloczyn_wudłużony = int(iloczyn*(10**n))
    iloczyn_obcięty = float(iloczyn_wudłużony/(10**n))

    return iloczyn_obcięty

print(rozw_dzies_iloczynu_do_n(8))

