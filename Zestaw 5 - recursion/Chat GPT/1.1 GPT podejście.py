def Labirynth(T):

    def rec(T,row,column):

        if row < 0 or column < 0 or row >= len(T) or column >= len(T) or T[row][column] == 0:
            return 0

        coins = T[row][column]
        max_coins = 0
        prev_coins = T[row][column]
        T[row][column] = 0

        if row == len(T)-1 and column == len(T)-1:
            return coins



        max_coins = max(max_coins,
                        rec(T,row-1,column), # UP
                        rec(T,row+1,column), # DOWN
                        rec(T,row,column-1), # LEFT
                        rec(T,row,column+1), # RIGHT
                        )

        T[row][column] = prev_coins

        return max_coins

    return rec(T,0,0)

board = [
  [1, 0, 2, 3],
  [2, 3, 0, 4],
  [5, 6, 7, 8],
  [0, 9, 8, 10]
]

print(Labirynth(board))