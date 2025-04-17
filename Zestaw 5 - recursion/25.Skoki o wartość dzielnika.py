def skoki_skibidii(T):

    def primes_list(num):

        i = 2
        list = []
        while num != 1:
            if num%i == 0:
                list.append(i)
                num//=i
                i -=1
            i+=1
        return list

    def reqjurzjon(T,index):
        wynik = 0
        factors = primes_list(T[index])

        for mech in factors:
            if mech == len(T)-1:
                return 1

        for bruh in factors:
            if index+bruh<len(T)-1:
                wynik += reqjurzjon(T[bruh:len(T)],0)

        if wynik>0:
            return True
        return False


    return reqjurzjon(T,0)


print(skoki_skibidii([6,17,19,3,4,2,5,17,17,17,17,7]))