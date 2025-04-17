def podział_num(number):

    T = [0]*number

    def reqjurzjon(number,i,T):
        if number == 0:
            print(T)

        if i == 0:
            mini=1
        else:
            mini=T[i-1]

        for j in range(mini,number+1):
            T[i] = j
            reqjurzjon(number-j,i+1,T)
            T[i]=0

    reqjurzjon(number,0,T)


podział_num(3)

