def przlicz_na_sys_liczbowy(num,sys):
    liczba = ''
    while num !=0:
        reszta = num%sys
        num //=sys
        if reszta >=10:
            reszta -= 10
            liczba = chr(ord('A')+reszta) + liczba

        else:
            liczba = str(reszta) + liczba

    return liczba

t1 = [1,2,3,4]
t2 = [9,7,4,8]

def poprawne_sumy_z_2_tablic(t1,t2):
    max_len = len(t1)
    b = []
    lista_sum = []

    for i in range (3**len(t1)):

        z = i
        s = 0
        for _ in range(max_len):
            b.append(z%3)
            z//=3
        for k in range (max_len):
            if b[k] == 0:
                s += t1[k] + t2[k]
            elif b[k] == 1:
                s += t1[k]
            else:
                s += t2[k]
        lista_sum.append(s)

    return lista_sum

print(poprawne_sumy_z_2_tablic(t1,t2))


