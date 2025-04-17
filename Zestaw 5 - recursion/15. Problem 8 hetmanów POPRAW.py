def eight_queens_set(T,w,last_row=-1,last_column=-1):

    if w>7:
        for bruh in T:
            print(bruh)
        return True

    if last_row == -1 and  last_column == -1:
        last_row,last_column = 0,0

    k = 0
    while k <8:
        if T[w][k] == 0:
            T[w][k] = 8

            for bruh in T:
                print(bruh)
            print('bruh')
            row_iterate = w+1
            while row_iterate < 8:
                T[row_iterate][k] = 1
                row_iterate +=1

            row_iterate = w+1
            column_iterate = k -1
            print(row_iterate,column_iterate)
            while row_iterate < 8 and column_iterate >0:
                T[row_iterate][column_iterate] = 1
                row_iterate += 1
                column_iterate -=1

            for bruh in T:
                print(bruh)
            print('bruh')

            row_iterate = w + 1
            column_iterate = k + 1
            while row_iterate < 8 and column_iterate <8:
                T[row_iterate][column_iterate] = 1
                row_iterate += 1
                column_iterate += 1

            for bruh in T:
                print(bruh)
            print('bruh')

            w +=1

            eight_queens_set(T,w,last_row,last_column)
        k +=1



T = [[0 for _ in range(8)] for _ in range (8)]

eight_queens_set(T,0,0,0)