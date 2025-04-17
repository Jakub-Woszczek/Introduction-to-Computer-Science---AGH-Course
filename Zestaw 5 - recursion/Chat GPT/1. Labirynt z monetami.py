# Napisz funkcję rekurencyjną, która przyjmuje labirynt w postaci siatki,
# a także aktualne położenie gracza w labiryncie. Funkcja powinna zwrócić
# maksymalną ilość monet, które gracz może zgromadzić, przechodząc od startu
# do mety, zgodnie z zasadami ruchu (góra, dół, lewo, prawo) i nie przechodząc
# przez pola z wartością "0".

def labirynt(T):

    def rec(T,row,column):
        coins = 0
        max_coins = 0
        if row == len(T)-1 and column == len(T)-1:
            return coins

        # UP
        if row -1 >=0 and T[row-1][column] != 0:
            prev_coin = T[row][column]
            T[row][column] = 0
            max_coins += max(max_coins,rec(T,row-1,column))
            T[row][column] = prev_coin

        # DOWN
        if row +1 < len(T) and T[row+1][column] != 0:
            prev_coin = T[row][column]
            T[row][column] = 0
            max_coins += max(max_coins,rec(T,row+1,column))
            T[row][column] = prev_coin

        # ->
        if column+1 < len(T) and T[row][column+1] != 0:
            prev_coin = T[row][column]
            T[row][column] = 0
            max_coins += max(max_coins,rec(T,row,column+1))
            T[row][column] = prev_coin

        # <-
        if column-1 >=0 and T[row][column-1] != 0:
            prev_coin = T[row][column]
            T[row][column] = 0
            max_coins += max(max_coins,rec(T,row,column-1))
            T[row][column] = prev_coin

        return max_coins





    return rec(T,0,0)


board = [
  [1, 0, 2, 3],
  [2, 3, 0, 4],
  [5, 6, 7, 8],
  [0, 9, 8, 10]
]

print(labirynt(board))