def czy_waga_taka_sama(s1,s2):
    litery_s1 = [litera for litera in s1]
    litery_s2 = [litera1 for litera1 in s2]

    asci_1 = 0
    asci_2 = 0

    for znak in litery_s1:
        asci_1 += ord(znak)

    for znak_2 in litery_s2:
        asci_2 += ord(znak_2)

    if asci_1 != asci_2:
        return False

    liczba_sam_1 = 0
    liczba_sam_2 = 0

    samogłoski = ['a','e','i','o','u','y']

    for literka in litery_s1:
        if literka in samogłoski:
            liczba_sam_1 +=1

    for literka_2 in litery_s2:
        if literka_2 in samogłoski:
            liczba_sam_2 +=1

    if liczba_sam_1 != liczba_sam_2:
        return False
    return True

def wyraz(s1,s2):
    litery_s1 = [litera for litera in s1]
    litery_s2 = [litera1 for litera1 in s2]
    wyraz = ''
    n = len(s2)

    def reqjurzjon(i,s1,s2,wyraz):

        if i > len(s2):
            return False


        if czy_waga_taka_sama(s1,wyraz) == True:
            return True

        # for i in range(len(s1)):


        return reqjurzjon(i+1,s1,s2,wyraz+s2[i]) or reqjurzjon(i+1,s1,s2,wyraz)

    return reqjurzjon(0,s1,s2,wyraz)

print(wyraz('exe','ulala'))

