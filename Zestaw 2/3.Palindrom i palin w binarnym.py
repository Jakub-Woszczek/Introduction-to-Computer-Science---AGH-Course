liczba_podana = int(input('Podaj liczbę: '))
def dłudługość_liczby(a):
    a = int(a)
    i=0
    while a>0:
        #liczba = a % 10
        a //= 10
        i+=1
    return i
def odwrócenie_liczby(a):
    długość_liczby_do_bin = dłudługość_liczby(a)
    a = int(a)
    n = 1
    next_odejmowanie = 0
    długość = dłudługość_liczby(a)
    liczba = 0
    cyfra_1 = 0
    while n <długość+1:

        cyfra = a // 10**(długość - n)
        next_odejmowanie = (cyfra//10)*10
        cyfra_1 =cyfra - next_odejmowanie
        liczba += cyfra_1*(10**(n-1))
        n +=1


    return liczba

if odwrócenie_liczby(liczba_podana) ==liczba_podana:
    print(f'Liczba {liczba_podana} jest palindromem :3')
else:
    print('Lliczba ta nie jest palindromem')


def dacimal_to_bianary(a):

    liczba_bin_odwrócona = ''
    while a > 0:
        number = str(a%2)
        a = a//2
        liczba_bin_odwrócona += number
    #liczba_bin = odwrócenie_liczby(liczba_bin_odwrócona)

    return liczba_bin_odwrócona



def dec_bin_dobre(liczba_podana):
    liczba_podana_bin_odwrócona = dacimal_to_bianary(liczba_podana)
    liczba_podana_bin_odwrócona = str(liczba_podana_bin_odwrócona)
    długość_binar_odwr = len(liczba_podana_bin_odwrócona)
    odwócona_podana_bez_zer = odwrócenie_liczby(liczba_podana)
    odwócona_podana_bez_zer = str(odwócona_podana_bez_zer)
    długość_binar_bez_zer = len(odwócona_podana_bez_zer)
    ilość_ucientych = int(długość_binar_odwr) - int(długość_binar_bez_zer)
    liczba_podana = str(liczba_podana)
    while ilość_ucientych>1:
        odwócona_podana_bez_zer += '0'

        ilość_ucientych -=1

    return liczba_podana


print(dec_bin_dobre(liczba_podana))



num = 3545  # Replace 42 with the integer you want to convert to binary
print(num.bit_length())
binary_num = bin(num)[2:]
print(10//3)

