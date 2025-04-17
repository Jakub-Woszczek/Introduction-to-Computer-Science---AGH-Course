# X -> Y w mniej niż N krokach

def parzyste_o_1(num):
    len = 0
    a = num
    while a != 0:
        a //=10
        len +=1
    end_num = 0
    for i in range(len):
        if (num%10)%2==0:
            end_num += (num%10+1)*(10**i)
        else:
            end_num += (num % 10) * (10 ** i)

        num//=10
    return end_num



def kolos_xd(X,Y,N):
    def reqjurzjon(num1,num2,N,prev_action):
        suma =0
        if num1 == num2:
            return 1

        if num1>num2:
            return 0

        if prev_action != 'A':
            suma += reqjurzjon(num1+3,num2,N,'A')

        if prev_action != 'B':
            suma += reqjurzjon(num1*2,num2,N,'B')

        if prev_action != 'C':
            suma += reqjurzjon(parzyste_o_1(num1),num2,N,'C')

        return suma

    return reqjurzjon(X,Y,N,0)

print(kolos_xd(11,32,4))

