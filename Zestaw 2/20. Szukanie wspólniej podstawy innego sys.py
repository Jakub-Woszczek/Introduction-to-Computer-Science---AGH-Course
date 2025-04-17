def przeliczanie_na_inny_sys(x,y):
    sys_dobry = []
    for sys in range(2,11):
        sys_dobry.append(sys)
        p = 0
        num1 =x
        num2 = y
        while num1 != 0:
            reszta1 = num1 % sys
            num1 //= sys
            b = num2
            while b !=0:
                reszta2 = b % sys
                b //= sys

                if reszta2 == reszta1 and p==0:
                    p += 1
                    sys_dobry.remove(sys)




    return sys_dobry

print(przeliczanie_na_inny_sys(15,16))

# for a in range(2,100):
#     for b in range(2,100):
#         print(przeliczanie_na_inny_sys(a, b))



