def rook(N,L):
    def tablica_z_listy(L):
        T = [[0 for _ in range(N)] for _ in range(N)]
        for mech in L:
            T[mech[0]][mech[1]] = 1

        return T

    T = tablica_z_listy(L)
    moves_T = T.copy()
    def reqjurzjon(T,moves_cnt,loc):
        mini = float('inf')
        row,column = loc
        moves_T[row][column] = 8



        if loc == [N-1,N-1]:
            # print(moves_cnt)
            return moves_cnt

        a = row+1
        while a<N and T[a][column] != 1:

            mini = min(mini, reqjurzjon(T,moves_cnt+1,[a,column]))
            a +=1

        b = column + 1
        while b<N and T[row][b] != 1:
            mini = min(mini, reqjurzjon(T, moves_cnt + 1, [row, b]))
            b += 1



        return mini



    return reqjurzjon(T,0,[0,0])

L = [[2,0],[1,3],[4,2],[3,3],[0,3]]

moves_cnt = rook(5,L)
print(moves_cnt)

# for bruh in moves_T:
#     print(bruh)