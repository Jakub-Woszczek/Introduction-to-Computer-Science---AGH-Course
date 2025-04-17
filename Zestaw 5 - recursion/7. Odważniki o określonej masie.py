def waga(T,mass_ex):

    def req(T,mass_ex,mass_curr,index):

        if index == len(T)-1 and mass_ex != mass_curr:
            return False

        if mass_ex == mass_curr:
            return True

        return req(T,mass_ex,mass_curr+T[index],index+1) or req(T,mass_ex,mass_curr,index+1)


    return req(T,mass_ex,0,0)

print(waga([1,2,3,4,56,3,2,62],670))



