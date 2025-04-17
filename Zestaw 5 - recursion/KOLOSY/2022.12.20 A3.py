def king(N,L):

    def tablica_z_listy(L):
        T = [[0 for _ in range(N)] for _ in range(N)]
        for mech in L:
            T[mech[0]][mech[1]] = 1

        return T

    def reqjurzjon(T,N,loc):
        row,column = loc
        T[row][column] = 8
        maxi = float('-inf')
        if loc == [N-1,N-1]:
            return True

        if row -1 >=0 and T[row-1][column] ==0:

            loc = [row-1,column]
            maxi = max(maxi, reqjurzjon(T,N,loc))

        if column+1 <N and T[row ][column+1] == 0:
            loc = [row, column+1]
            maxi = max(maxi, reqjurzjon(T, N, loc))

        if row + 1 < N and T[row + 1][column] == 0:
            loc = [row + 1, column]
            maxi = max(maxi, reqjurzjon(T, N, loc))


        return maxi

    return reqjurzjon(tablica_z_listy(L),N,[0,0])

N = 5
L = [[0,1],[0,2],[0,3],[1,3],[2,3],[3,0],[3,1]]

print(king(N,L))