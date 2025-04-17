def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return True


def wykreślanie_cyfr(num):

    długość = 0
    a = num
    while a >0:
        długość +=1
        a //=10

    if długość>=3:
        bez_tyłu = num // 10
        if is_prime(bez_tyłu) == True:
            print(bez_tyłu)
        # wykreślanie_cyfr(bez_tyłu)

        bez_przodu = num % (10 ** (długość - 1))
        if is_prime(bez_przodu) == True:
            print(bez_przodu)
        # wykreślanie_cyfr(bez_przodu)

        for i in range(2, długość):
            prawa = num % (10 ** (i - 1))
            lewa = (num // (10 ** i)) * 10 ** (i - 1)
            cała = lewa + prawa
            if is_prime(cała) == True:
                print(cała)
            wykreślanie_cyfr(cała)


wykreślanie_cyfr(12345)