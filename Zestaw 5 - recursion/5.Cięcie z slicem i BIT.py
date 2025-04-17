def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def binary_to_decimal(binary_list):
    binary_string = ''.join(map(str, binary_list))  # Konwersja listy na string binarny
    decimal_number = int(binary_string, 2)  # Konwersja stringa binarnego na liczbę dziesiętną
    return decimal_number

def decimal(binary):
    binary = binary_to_decimal(binary)
    decimal = 0
    power = 0
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        binary //= 10
        power += 1
    return decimal

def zad5(T):

    def requrzjon(T,i,j):

        if j == len(T)-1:
            if T[j-1] == 0 and j-i != 1:
                return False
            return is_prime(decimal(T[i:j+1]))

        if is_prime(decimal(T[i:j+1])):
            return requrzjon(T[j+1:len(T)],0,0)


        return (requrzjon(T[i:len(T)],i,j+1))


    return requrzjon(T,0,0)

print(zad5([1,1,1,0,1,1]))