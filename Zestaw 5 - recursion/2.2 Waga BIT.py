def waga(num):
    prime_factors = 0
    i = 2
    prev_factor = 0
    while num != 1:
        if num % i == 0:
            num //= i
            i-=1
            if i != prev_factor:
                prime_factors +=1
            prev_factor = i

        i +=1

    return prime_factors

print(waga(1))

def zadanko_2(T):

    n = len(T)

    def reqjurzjon(i,A,B,C):

        if i == n:
            return A == B and B == C

        return reqjurzjon(i+1,A + waga(T[i]),B,C) \
                or reqjurzjon(i+1,A,B+ waga(T[i]),C) \
                or reqjurzjon(i+1,A,B,C+ waga(T[i]))

    return reqjurzjon(0,0,0,0)

print(zadanko_2([2,17,6,5,10,6]))