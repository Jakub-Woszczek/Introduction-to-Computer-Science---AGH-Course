def czy_liczba_jest_podciągniem(num):
    a = 1
    b = 1
    sum = 0
    while sum<num:

        sum += a
        a,b = b,a+b

    if sum == num:
        return True
    else:
        a = 1
        b = 1
        while sum > num:
            sum -= a
            a, b = b, a + b
        if sum == num:
            return True
        else:
            return False

def czy_liczba_to_fib(num):
    a= 1
    b = 1

    while a<num:
        a,b = b,a+b
    if a == num:
        return True
    else:
        return False


def nastepna_ktora_nie_jest_podciagiem(num):

    if czy_liczba_to_fib(num) == True:
        print("ta liczba jest w fib :3")

    else:
        podstawnik = num
        while num != 1:

            if czy_liczba_jest_podciągniem(podstawnik) == True and podstawnik !=num:

                return podstawnik
            #print(podstawnik)
            podstawnik += 1

liczba_nat = int(input("odaj liczbę: "))

natępnabez_podciągu = nastepna_ktora_nie_jest_podciagiem(liczba_nat)

print(f"liczba {natępnabez_podciągu} jest następna po {liczba_nat} dla której nie ma podciągu ")

