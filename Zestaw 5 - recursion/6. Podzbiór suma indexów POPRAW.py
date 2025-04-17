# def suma_index(T):
#     # sum_tablicy = 0
#     # for i in range(len(T)-1):
#     #     sum_tablicy += T[i]
#     def rek (T,cnt,sum_index,sum_numbrs,index):
#
#         if index >= len(T)-1 and sum_index != sum_numbrs:
#             return float('inf')
#         # print(sum_index,sum_numbrs)
#         if sum_index == sum_numbrs and index == len(T) and cnt != 0:
#             return cnt
#
#
#         include_current = rek(T, cnt + 1, sum_index + index, sum_numbrs + T[index], index + 1)
#         exclude_current = rek(T, cnt, sum_index, sum_numbrs, index + 1)
#
#         return min(include_current, exclude_current)
#
#     return rek(T,0,0,0,0)
#
# T = [ 1,3,0,2]
#
# print(suma_index(T))

##################

def suma_v2(T):
    suma = 0

    def rek(T,cnt,suma_indx,suma_liczb,index):

        if suma_indx == suma_liczb and suma_liczb !=0:
            return cnt

        if index == len(T)-1:
            return 20

        # suma += rek(T,cnt,suma_indx,suma_liczb,index+1)
        # suma += rek(T,cnt+1,suma_indx+index,suma_liczb+T[index],index+1)

        return min(rek(T,cnt,suma_indx,suma_liczb,index+1),rek(T,cnt+1,suma_indx+index,suma_liczb+T[index],index+1))

    return rek(T,0,0,0,0)
T = [ 0,1,2,3]
T = [  1,7,3,5,11,2]
print(suma_v2(T))