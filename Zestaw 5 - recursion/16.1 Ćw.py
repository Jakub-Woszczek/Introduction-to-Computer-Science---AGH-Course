# Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek
# oraz sumy kodów ascii liter z których są zbudowane są identyczne

#  Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe
# zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co
# wyraz s1. Dodatkowo funkcja powinna wypisać znaleziony wyraz.

def waga(s1,s2):
    ASCI_1 = 0
    ASCI_2 = 0
    for letter in s1:
        ASCI_1 += ord(letter)

    for letter in s2:
        ASCI_2 += ord(letter)

    if ASCI_1 != ASCI_2:
        return False

    liczba_sam_1 = 0
    liczba_sam_2 = 0

    samogłoski = ['a', 'e', 'i', 'o', 'u', 'y']

    for literka in s1:
        if literka in samogłoski:
            liczba_sam_1 += 1

    for literka_2 in s2:
        if literka_2 in samogłoski:
            liczba_sam_2 += 1

    if liczba_sam_1 != liczba_sam_2:
        return False
    return True

def wyraz(s1,s2):
    # letters_s1 = [letter for letter in s1]
    # letters_s2 = [letter for letter in s2]

    wyraz = ''


    def reqjurzjon(s1,s2,wyraz,i):

        if i == len(s2)-1:
            if waga(s1,wyraz):
               return True
            return False

        return reqjurzjon(s1,s2,wyraz + s2[i],i+1) or reqjurzjon(s1,s2,wyraz,i+1)

    return reqjurzjon(s1,s2,wyraz,0)

print(wyraz('exe','ulalalalalalalal'))