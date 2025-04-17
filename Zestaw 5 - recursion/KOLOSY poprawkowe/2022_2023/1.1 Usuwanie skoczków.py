def usun(T,N):
    szchownica = [[0 for _ in range(N)] for _ in range(N)]

    def ilosc_pul_od_ustawnienia(T_polozenia, N):
        T = [[-2, 1], [-2, -1], [-1, 2], [1, 2], [2, -1], [2, 1], [1, -2], [-1, -2]]
        szchownica_v2 = [[0 for _ in range(N)] for _ in range(N)]

        for place in T_polozenia:
            row, col = place
            szchownica_v2[row][col] = 2
            for bicie in T:
                row_b, col_b = bicie

                if (row + row_b) < len(szchownica_v2) and (row + row_b) >= 0:
                    if (col + col_b) < len(szchownica_v2) and (col + col_b) >= 0:
                        if szchownica_v2[row + row_b][col + col_b] == 0:
                            szchownica_v2[row + row_b][col + col_b] = 1

        cnt = 0
        for i in range(N):
            for j in range(N):

                if szchownica_v2[i][j] == 1:
                    cnt += 1

        for row in szchownica_v2:
            print(row)
        return cnt


ilp


