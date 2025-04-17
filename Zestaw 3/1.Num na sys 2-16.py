def przelicz_na_system(num, s):
        result = ''

        while num != 0:
            next_digit = num % s
            num //= s
            if next_digit >= 10:
                next_digit -= 10
                result = chr(ord("A") + next_digit) + result
            else:
                result = str(next_digit) + result

            # print(str(next_digit))

        return result



tablica_sys = []

for i in range(2,17):
    tablica_sys.append(i)

N = int(input('Podaj liczbe: '))
for a in range(len(tablica_sys)):
    sys = tablica_sys[a]
    print(f'liczba {N} w sys {sys} = {przelicz_na_system(N,sys)}')







