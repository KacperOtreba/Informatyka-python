# 07. Sortowanie przez scalanie
# Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4


# def scal(T,l,srodek,p):
#     i = l
#     j = srodek + 1
#     k = l
#     while i <= srodek and j <= p:
#         if T[i] < T[j]:
#             pom[k] = T[i]
#             i += 1
#         else:
#             pom[k] = T[j]
#             j += 1
#         k += 1
#     while i <= srodek:
#         pom[k] = T[i]
#         i += 1
#         k += 1
#     while j <= p:
#         pom[k] = T[j]
#         j += 1
#         k += 1
#     for i in range(l,p+1):
#         T[i] = pom[i]
#
# def sortuj(T,l,p):
#     if l < p:
#         srodek = (l+p)//2
#         sortuj(T,l, srodek)
#         sortuj(T,srodek+1,p)
#         scal(T,l,srodek, p)


# Zadanie 1
# Napisz program, który wczyta z klawiatury ciąg liczb rozdzielonych spacjami, a następnie posortuje
# ten ciąg za pomocą algorytmu przedstawionego w przykładzie i wyświetli po posortowaniu.

def scal(t1,t2):
    wynik = []
    i = 0
    j = 0
    n1 = len(t1)
    n2 = len(t2)
    while i < n1 and j < n2:
        if t1[i] < t2[j]:
            wynik.append(t1[i])
            i += 1
        else:
            wynik.append(t2[j])
            j += 1
    wynik.extend(t1[i:])
    wynik.extend(t2[j:])
    return wynik

def sortuj(t):
    n = len(t)
    if n > 1:
        srodek = (n-1) // 2
        lewy = sortuj(t[0:srodek+1])
        prawy = sortuj(t[srodek+1:])
        return scal(lewy,prawy)
    return t

print("Zadanie 1\n")
ciag = input("Podaj ciąg do posortowania: ")
ciag = list(map(int,ciag.split()))
pom = [0] * (len(ciag))
n = len(ciag)
ciag = sortuj(ciag)
print(ciag)


# Zadanie 2
# Napisz program w języku Python, który wczyta dwa uporządkowane niemalejąco ciągi liczb
# całkowitych, rozdzielonych spacją z pliku ciagi.txt . Następnie program wyświetli oraz zapisze do pliku
# winiki_2.txt ciąg liczb rozdzielonych spacjami, uporządkowany niemalejąco, składający się z liczb obu
# wczytanych ciągów. Nie musisz wykorzystywać pseudokodu z przykładu.
print("Zadanie 2\n")

plik = open("ciagi.txt","r")
ciag1 = plik.readline().rstrip()
ciag2 = plik.readline().rstrip()
ciag1 = list(map(int,ciag1.split()))
ciag2 = list(map(int,ciag2.split()))
plik.close()

print(ciag1)
print(ciag2)
plik = open("wyniki_2.txt","w")
wynik = scal(ciag1, ciag2)
print(wynik)
plik.write(" ".join(map(str, wynik)))
plik.close()

# Zadanie 3
# Napisz program w języku Python, który wylosuje milion liczb z zakresu od 1 do miliona, a następnie
# program zapisze ten ciąg posortowany metodą sortowania przez scalanie do pliku wyniki_3.txt (liczby
# w osobnych liniach).
print("Zadanie 3\n")
from random import randint

liczby = []
for i in range(1000): # 1000000
    liczby.append(randint(1,1000000))
liczby = sortuj(liczby)
plik = open("wyniki_3.txt","w")
for n in liczby:
    plik.write(f"{n}\n")


# Zadanie 4
# https://zadania.dlamaturzysty.info/s/5159/81431-informatyka/5040154-zadania-z-informatyki-Analiza-algorytmow.htm?podstr=6
print("Zadanie 4\n")
print("Nie ma kodu")

# Zadanie 5
# Napisz program wykonujący sortowanie ciągu liczbowego metodą sortowania przez scalanie bez
# korzystania z dodatkowej pamięci podczas scalania.
