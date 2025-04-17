def wyznacznik_macierzy(T):
    det = 0
    if len(T) == 2:
        for bruh in T:
            print(bruh)
        print('\n')
        return T[0][0]*T[1][1]-T[1][0]*T[0][1]

    for i in range(len(T)):
        det += ((-1)**(i))*(T[i][0])*wyznacznik_macierzy([row[:0] + row[1:] for row in T[:i] + T[i+1:]])

    return det

matrix = [
    [12, 42, 3],
    [4, 55, 46],
    [7, 8, 93]
]

# print(wyznacznik_macierzy(matrix))


import random

# Utwórz pustą macierz 5x5
matrix_5x5 = [[4] * 4 for _ in range(4)]

# Wypełnij macierz losowymi liczbami
for i in range(4):
    for j in range(4):
        matrix_5x5[i][j] = random.randint(1, 100)  # Zakres od 1 do 100 (możesz dostosować zakres)

# Wyświetl macierz
for row in matrix_5x5:
    print(row)

print(wyznacznik_macierzy(matrix_5x5))

print(wyznacznik_macierzy(matrix))