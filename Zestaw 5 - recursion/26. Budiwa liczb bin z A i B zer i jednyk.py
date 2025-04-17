# A-1 B-0

def is_composite(bin_num):
    liczba = 0
    i = 0
    while bin_num != 0 :
        digit = bin_num%10
        liczba += digit*(2**i)
        i+=1
        bin_num//=10
    divide = 2
    prev_div = 0
    print(liczba)
    while liczba != 1:
        if liczba%divide == 0:
            if divide == prev_div:
                return True
            liczba /=divide
            prev_div = divide
            divide -=1

        divide +=1
    return False

def bin(liczba,A,B):

    if A == 0 and B == 0:
        print(liczba)
        if is_composite(liczba) == True:
            return 1


    if liczba == 0:
        liczba = 1
        A -=1
    sum = 0
    if A>0:
        liczba_1 =liczba*10+1
        sum += bin(liczba_1,A-1,B)
    if B>0:
        liczba_2 = liczba*10
        sum += bin(liczba_2, A, B-1)

    return sum

print(bin(0,2,4))







print(is_composite(101011))