def weight(T,index,s1,s2,s3):

    if index == len(T):
        if s1 == s2 and s2 == s3:
            print(s1)
            return s1
        else:
            return False

    for i in range(3):

        if i == 0:
            s1 += T[index]
            index +=1

            weight(T,index,s1,s2,s3)
            index -=1
            s1 -= T[index]

        if i == 1:
            s2 += T[index]
            index += 1

            weight(T, index, s1, s2, s3)
            index -= 1
            s2 -= T[index]

        if i == 2:
            s3 += T[index]
            index += 1

            weight(T, index, s1, s2, s3)
            index -= 1
            s3 -= T[index]
    return s1
T = [1,5,4,9,6,5]
print(weight(T,0,0,0,0))