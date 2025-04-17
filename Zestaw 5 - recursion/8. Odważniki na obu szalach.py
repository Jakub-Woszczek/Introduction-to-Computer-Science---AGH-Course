def waga(T,mass_ex):

    def req(T,mass_ex,mass_curr,index):
        print(mass_ex,mass_curr,index)
        if index == len(T) and mass_ex != mass_curr:
            return False

        if mass_ex == mass_curr:
            return True

        return req(T,mass_ex,mass_curr+T[index],index+1) or req(T,mass_ex,mass_curr,index+1) or req(T,mass_ex+T[index],mass_curr,index+1)


    return req(T,mass_ex,0,0)

print(waga([1,2,4,56,3,62],60))



