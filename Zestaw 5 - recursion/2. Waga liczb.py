def ile_rożnych_pierwszych(num):
    factor = 2
    list_factors = []
    factors_count = 0
    while num !=1:

        if num%factor ==0:
            num //=factor
            factor -=1

            if factor not in list_factors:
                list_factors.append(factor)
                factors_count += 1

        factor +=1
    return factors_count


def diffrent_weights_of_list(T):


    if type(T[0]) == int:
        for index in range(len(T)):
            print(index)
            T[index] = [T[index],0]

    index = 0
    if T[len(T)-1][1] == 1:
        index = len(T)
    else:
        while T[index][1] != 0:
            index += 1

    if index == len(T):
        check_list = []
        for bruch in range(len(T)):
            number = T[bruch][0]
            if number not in check_list:
                check_list.append(number)
        if len(check_list) == 3:
            return True
        else:
            return False


    T[index] = [ile_rożnych_pierwszych(T[index][0]),0]
    print(T[index][0])
    print(T)
    T[index][1] = 1

    return  diffrent_weights_of_list(T)


# print(ile_rożnych_pierwszych(42))

print(diffrent_weights_of_list([15,7,42,26,5]))
