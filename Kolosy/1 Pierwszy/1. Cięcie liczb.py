def cięcie_num(num):

    a = num
    len_1 = 0
    while a !=0:
        a //=10
        len_1 +=1

    for p in range(len_1+1):
        num_ciecie_prawo  =num//(10**p)
        len_2 = len_1 - p

        for k in range(1,len_2+1):
            num_end = num_ciecie_prawo-(num_ciecie_prawo//(10**k))*(10**k)

            print(num_end)


cięcie_num(12345)