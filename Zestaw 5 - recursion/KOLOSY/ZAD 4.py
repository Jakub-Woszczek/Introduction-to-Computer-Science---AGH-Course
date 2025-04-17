def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def divide(N):

    def reqjurzjon(num,count_divs):

        if is_prime(num) == True and count_divs >0:
            return True
        factor = 10
        while factor<num//10:
            if is_prime(num%factor) == True:
                if reqjurzjon(num//factor,count_divs+1):
                    return reqjurzjon(num//factor,count_divs+1)
            factor*=10

            if factor*10>num:
                return False





    return reqjurzjon(N,0)

print(divide(23672))