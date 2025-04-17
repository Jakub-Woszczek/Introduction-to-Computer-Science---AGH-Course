def wartość_funkcji_homo(x):
    y = 1/x
    return y

def iloś_odc(k):
    k = int(k)
    długość = k-1

    for n in range(1,10**10):
        if długość/n <= 0.1:
            ilość_odc = n
            return ilość_odc


def pole_pod_wykresem(granica):
    granica = int(granica)
    sum_wartości = 0
    ilość_odcinków = iloś_odc(granica_prawa)
    długość_jednego_odc = (granica-1)/ilość_odcinków
    pierwszy_argument_srodkowy = 1 + ((granica - 1) / ilość_odcinków) / 2
    ostatni_arg_środkowy = pierwszy_argument_srodkowy + (ilość_odcinków-1)*długość_jednego_odc
    while pierwszy_argument_srodkowy<granica:

        sum_wartości += wartość_funkcji_homo(pierwszy_argument_srodkowy)
        pierwszy_argument_srodkowy += długość_jednego_odc

    pole_cał = długość_jednego_odc*sum_wartości
    return pole_cał

granica_prawa = input("podaj prawą granicę: ")

print(f"Pole pod wykresem od 1 do {granica_prawa} wynosi {pole_pod_wykresem(granica_prawa)}")