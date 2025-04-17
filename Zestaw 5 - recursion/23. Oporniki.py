def possible_resistors_configs(T,Rw,l=0,index=0):

    if l == 3:
        print(Rw)
        return Rw

    R = T[index]
    if Rw == 0:
        Rw = R
        index +=1
        l +=1
        R = T[index]
        # possible_resistors_configs(T,Rw,l+1,index+1)

    if l<3:
        # l+=1

        possible_resistors_configs(T, Rw + R, l + 1,index+1)

        possible_resistors_configs(T, (Rw * R) / (Rw + R), l + 1,index+1)

    return Rw

possible_resistors_configs([1,2,3],0,0,0)