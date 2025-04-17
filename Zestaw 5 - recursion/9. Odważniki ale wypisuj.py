def waga(T,mass_ex):
    list_weights = []
    def req(T,mass_ex,mass_curr,index,list_weights):

        if index == len(T) and mass_ex != mass_curr:
            return False

        list_weights_2_bez = list_weights.copy()
        list_weights_2_z = list_weights.copy()
        list_weights_2_z.append(T[index])

        if mass_ex == mass_curr:
            return True, list_weights

        return (req(T,mass_ex,mass_curr+T[index],index+1,list_weights_2_z)
                or req(T,mass_ex,mass_curr,index+1,list_weights_2_bez)
                or req(T,mass_ex+T[index],mass_curr,index+1,list_weights_2_z))


    return req(T,mass_ex,0,0,[])

print(waga([1,2,4,56,3,62],60))



