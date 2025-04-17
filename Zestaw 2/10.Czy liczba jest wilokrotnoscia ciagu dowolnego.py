def nty_wyraz_ciągu(n):
    if n == 1:
        return 2
    A = 3*(nty_wyraz_ciągu(n-1))+1

    return A

def czy_liczba_jest_wyrazem_ciągu(num):
    wartość_wyrazu = 2

    while wartość_wyrazu < num:
        wartość_wyrazu = wartość_wyrazu*3+1

    if wartość_wyrazu == num:
        return True

def czy_jest_wielokrotnością(num):
    if czy_liczba_jest_wyrazem_ciągu(num) == True:
        return True
    else:
        n = 1
        lista_wiel = []
        while nty_wyraz_ciągu(n)<num:

            który_z_kolei = 1
            wielokrotność_wyrazu = nty_wyraz_ciągu(n)
            suma = nty_wyraz_ciągu(n)
            while wielokrotność_wyrazu <num:
                wielokrotność_wyrazu += suma
                który_z_kolei +=1

            if wielokrotność_wyrazu == num:
                lista_pojedyńcza = [int(num/który_z_kolei),który_z_kolei]
                lista_wiel.append(lista_pojedyńcza)
                # lista_wiel = lista_wiel + lista




            n += 1

        if lista_wiel == []:
            return False
        else:
            return lista_wiel






print(czy_jest_wielokrotnością(1420738))