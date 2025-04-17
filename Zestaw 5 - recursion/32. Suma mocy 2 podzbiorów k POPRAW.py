def zad23(T,k):

    def next_f(T,k,a,b,index = 0):
        # pusta_dodanie = [0 for _ in range(len(T))]
        # a = [0 for _ in range(len(T))]
        # b = [0 for _ in range(len(T))]
        if index > len(T):
            return False

        if k == 0 :
            if a == b:
                return True
            return False

        return next_f(T,k-1,a+T[index],b,index+1) \
                or next_f(T,k-1,a,b+T[index],index+1)

    return next_f(T,k,0,0,0)

print(zad23([1,3,8,2,1,13,2],7))