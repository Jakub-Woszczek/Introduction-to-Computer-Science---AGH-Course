def knight(T,step,row=0,column=0):
    lista_ruchów = []
    # for mech in T:
    #     print(mech)
    # print('Mech')

    T[row][column] = step
    lenght_T = len(T)
    if step == lenght_T**2:
        return T

    possible_movments = [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]

    for bruh in possible_movments:
        new_row = row + bruh[0]
        new_column = column + bruh[1]
        if -1 < new_row < lenght_T and -1 < new_column < lenght_T:
            # print(row,column)
            # print(T[row + bruh[0]][column + bruh[1]])
            if T[new_row][new_column] == 0:
                M = knight(T,step+1,new_row,new_column)

                if M != False:
                    return M
                else:
                    T[new_row][new_column]=0
    return False

T = [[0 for _ in range(5)] for _ in range(5)]

ruchy = (knight(T,1,0,0))

for bruh in ruchy:
    print(bruh)