def how_long(num):
    dlugość = 0
    while 0 != num:
        num //=10
        dlugość +=1

    return dlugość

def erase_digits(mask,number):
    ending_num = 0
    if mask == 0:
        return ending_num
    print(mask)
    if mask % 10 == 1:
        ending_num += number % 10
        mask //= 10
        number //= 10
        # print(erase_digits(mask,number))

    else:
        # ending_num += number%(10**(i+1))
        mask //= 10
        number //= 10

    ending_num = erase_digits(mask, number)


    return ending_num

print(erase_digits(1001101,1234567))


def maska_bitowa(len,num,A,B):

    if how_long(num) == len:
        return num

