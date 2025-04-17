def sumy_i_reprezentacje(t1, t2):
    max_len = max(len(t1), len(t2))
    sumy = []
    reprezentacje = []

    for i in range(3 ** max_len):
        b = []
        z = i
        for _ in range(max_len):
            b.append(z % 3)
            z //= 3

        current_sum = 0
        for k in range(max_len):
            if k < len(t1):
                if b[k] == 0:
                    current_sum += t1[k] + t2[k]
                elif b[k] == 1:
                    current_sum += t1[k]
                else:
                    current_sum += t2[k]
            elif k < len(t2):
                if b[k] == 0:
                    current_sum += t2[k]
                elif b[k] == 1:
                    current_sum += t1[k]
                else:
                    current_sum += t2[k]

        sumy.append(current_sum)
        reprezentacje.append(b)

    return sumy, reprezentacje


t1 = [1, 2, 3, 4]
t2 = [9, 7, 4, 8]
sumy, reprezentacje = sumy_i_reprezentacje(t1, t2)

for i in range(len(sumy)):
    print(f"Suma: {sumy[i]}, Reprezentacja: {reprezentacje[i]}")
