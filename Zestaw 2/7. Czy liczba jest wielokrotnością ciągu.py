import math

liczba_podana = int(input("podaj liczbę: "))

pier_z_delty = math.sqrt(4+(liczba_podana-1))

if pier_z_delty == int(pier_z_delty):
    print(f'Liczba {liczba_podana} jest wielokrotnością tego ciągu')


elif 1==1:

    for i in range(1,int(liczba_podana/2)+1):
        kolejny_wyraz = i*i + i + 1
        if liczba_podana/kolejny_wyraz == int(liczba_podana/kolejny_wyraz):

            wielokrotność = int(liczba_podana/kolejny_wyraz)

            print(f'Liczba {liczba_podana} jest {wielokrotność} wielokrotnością tej liczbyj')

else:
    print('liczba nie jest wieloktonością tej liczcby')




# for n in range(0,101):
#     kolejny_wyraz = n*n+n+1
#     print(kolejny_wyraz)