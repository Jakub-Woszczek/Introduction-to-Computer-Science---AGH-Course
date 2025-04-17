liczba = 100000000
lewa_gr = 0
lewa_gr = int(lewa_gr)
prawa_gr = 0
prawa_gr = int(prawa_gr)
argument = None
i = 0
while (lewa_gr>=0 and prawa_gr >=0) or (lewa_gr<=0 and prawa_gr <=0):
    i += 1
    lewa_gr = prawa_gr
    prawa_gr = i**i-liczba
print(lewa_gr,prawa_gr,i)

prawa_gr = i
lewa_gr = prawa_gr-1
srednia_ar = None
x = None
while abs(prawa_gr**prawa_gr-liczba)>1:
    srednia_ar = (lewa_gr + prawa_gr)/2
    x = srednia_ar**srednia_ar-liczba
    if x >0:
        prawa_gr = srednia_ar
    else:
        lewa_gr = srednia_ar
print(prawa_gr)

