def smallest(T):
    n = len(T)
    def rek(sum_el,sum_index,cnt,index):

        if index == n :
            return (sum_el, cnt) if sum_el == sum_index and cnt>0 else (10000, 10000)

        sum_v1, cnt_1 = rek(sum_el,sum_index,cnt,index+1)
        sum_v2, cnt_2 = rek(sum_el+T[index],sum_index+index,cnt+1,index+1)

        return (sum_v1, cnt_1) if  cnt_1<=cnt_2 else (sum_v2, cnt_2)

    sum_v, _ = rek(0,0,0,0)

    return sum_v

print(smallest([1,7,3,5,11,2]))