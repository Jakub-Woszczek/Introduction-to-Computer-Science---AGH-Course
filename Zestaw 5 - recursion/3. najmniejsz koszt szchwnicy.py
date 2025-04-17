def smalest_king_transition_of_3(T,wiersz,kolumna):

    if wiersz == 2:
        return T[wiersz][kolumna]

    for i in range(3):

        if i == 0 and kolumna-1>=0:

            liczba = smalest_king_transition_of_3(T,wiersz+1,kolumna-1)

        if i == 1:

            liczba = smalest_king_transition_of_3(T,wiersz+1,kolumna)

        if i == 2 and kolumna+1<len(T):

            liczba = smalest_king_transition_of_3(T,wiersz+1,kolumna+1)
    list_of_nums = []

    list_of_nums.append(liczba)

    return list_of_nums

print(smalest_king_transition_of_3([[1,2,3],[8,9,10],[4,7,5]],0,1))

