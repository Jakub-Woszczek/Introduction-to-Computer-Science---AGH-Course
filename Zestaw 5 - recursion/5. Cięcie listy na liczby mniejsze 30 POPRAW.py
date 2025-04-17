# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.

def is_prime_form_bin(liczba_binarna):
    print(f"liczba bin: {liczba_binarna}")

    decimal = 0
    power = 0
    while liczba_binarna > 0:
        last_digit = liczba_binarna % 10
        decimal += last_digit * (2 ** power)
        liczba_binarna //= 10
        power += 1



    if decimal <= 1:
        return False

    for i in range(2, int(decimal ** 0.5) + 1):
        if decimal % i == 0:
            return False

    return True


def sliceing(T,i):
    print(T)
    a =i - 1
    p = 0
    bin = 0
    while a >= 0:
        print(a)
        bin += T[a]*(10**p)
        a -=1
        p +=1

    T_1 = [T[m] for m in range(len(T)) if m>=i]

    print(bin)


    return bin,T_1




def cutting_array(T,iterator):
    wynik = 0
    print(T)
    print(f"iterator {iterator}")

    if iterator == len(T)-2:
        bin_last,T_last = sliceing(T,iterator)
        if T_last[0] == 1 and T_last[1] == 1:
            if is_prime_form_bin(bin_last) == True:
                return 1
            return 0



    if iterator < 4:
        wynik += cutting_array(T,iterator+1)

    bin,T_1 = sliceing(T,iterator)

    if is_prime_form_bin(bin) == True:
        wynik += cutting_array(T_1,0)


    if wynik>0:
        return True
    return False

print(cutting_array([1,1,0,1,0,0],0))