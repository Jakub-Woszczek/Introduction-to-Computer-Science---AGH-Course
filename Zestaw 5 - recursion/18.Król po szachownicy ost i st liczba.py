def czy_ostatnia(num1,num2):
    digit_2 = 0
    while num2 != 0:
        digit_2 = num2%10
        num2 //=10

    digit_1 = num1%10

    if digit_1 < digit_2:
        return True
    return False

def does_path_exist(T,Ruchy,w=0,k=0):

    Ruchy[w+k] = [w,k]
    table_path = T.copy()
    table_path[0][0] = 0
    l = len(T)
    if w == 3 and k == 3:
        for bruh in table_path:
            print(bruh)
        print('True')
        print(Ruchy)
        return 1

    sum = 0
    if w + 1 < l:
        if czy_ostatnia(T[w][k], T[w + 1][k]) == True:
            table_path[w+1][k] = 0
            sum += does_path_exist(T, w + 1, k)


    if k + 1 < l and w + 1 < l:
        if czy_ostatnia(T[w][k], T[w + 1][k + 1]) == True:
            table_path[w + 1][k+1] = 0
            sum += does_path_exist(T, w + 1, k + 1)


    if k + 1 < l:
        if czy_ostatnia(T[w][k], T[w][k + 1]) == True:
            table_path[w][k+1] = 0
            sum += does_path_exist(T, w , k + 1)

    if sum >0:

        return True
    return False

board = [
    [123, 456, 781, 111],
    [222, 331, 441, 555],
    [666, 771, 881, 991],
    [101, 201, 303, 404]
]
len = len(board)*2
print(len)
ruchy = [0 for _ in range(len*2)]
print(ruchy)
print(does_path_exist(board,ruchy))
