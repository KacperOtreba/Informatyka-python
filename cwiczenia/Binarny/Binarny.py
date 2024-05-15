def lenik(napis):
    d = 0
    for i in napis:
        d+=1
    return d

def suma1(napis):
    ile = 0
    for i in napis:
        if i == 1:
            ile+=1
    return ile






print("Zadanie 1")
def LiczbaBlokow(n):
    ile = 1
    for i in range(lenik(n)-1):
        if (n[i] != n[i+1]):
            ile += 1
    return ile

print(LiczbaBlokow("1110011"))



print("Zadanie 2")
with open("F:/Informatyka-python/cwiczenia/Binarny/bin.txt") as f:
    T = f.read().split()

ileblokow = 0
for i in T:
    if (LiczbaBlokow(i) <= 2):
        ileblokow += 1
print(ileblokow)




print("Zadanie 3")
# najdluzszy = T[0]     # To jest źle
# najdluzsze = []
# for i in T:
#     if (lenik(i) > lenik(najdluzszy)):
#         najdluzsze = []
#         najdluzsze.append(i)
#     if (lenik(i) == lenik(najdluzszy)):
#         najdluzsze.append(i)


# najwiecej1 = najdluzsze[0]
# for i in najdluzsze:
#     if (suma1(i) > suma1(najwiecej1)):
#         najwiecej1 = i

# print(najwiecej1)
with open("F:/Informatyka-python/cwiczenia/Binarny/bin.txt") as f:
    T = f.read().split()


def wieksza(a,b):
    if lenik(a) > lenik(b):
        b = "0"* (lenik(a)-lenik(b)) + b
    else:
        a = "0"* (lenik(b)-lenik(a)) + a
    
    for i in range(lenik(a)):
        if a[i] == "1" and b[i] == "0":
            return True
        elif a[i] == "0" and b[i] == "1":
            return False
    return False

najwieksza = T[0]
for i in T:
    if (wieksza(i,najwieksza)):
        najwieksza = i
print(najwieksza)




print("Zadanie 4")

def odwrot(napis):
    odwrocona = ""
    for i in range(lenik(napis)-1,-1,-1):
        odwrocona += napis[i]
    return odwrocona


def czyPalindrom(napis):
    if (napis == odwrot(napis)):
        return True
    else:
        return False


napis = "1234567"
czyDaSie = False

if (napis == odwrot(napis)):
    print(f"{napis} jest palindromiczna")
else:
    print(f"{napis} nie jest palindromiczna")

if (odwrot(napis) == napis):
    pass
else:
    for i in range(lenik(napis)+1):
        tymczasowaZBitem = napis[:i] + "0" + napis[i:]
        if czyPalindrom(tymczasowaZBitem):
            print("Da się wstawić bit (0) i będzie palindromem")
            czyDaSie = True
            break
    for i in range(lenik(napis)+1):
        tymczasowaZBitem = napis[:i] + "1" + napis[i:]
        if czyPalindrom(tymczasowaZBitem):
            print("Da się wstawić bit (1) i będzie palindromem")
            czyDaSie = True
            break
    if (czyDaSie == False):
        print("Nie da się wstawić nic żeby była palindromem")



print("Zadanie 5")
