# 05. Wyszukiwanie binarne
    # Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4
import random

T = []
def czyNiemalejaca(T):
    for i in range(0,len(T)-1):
        if T[i] > T[i+1]:
            return False
    return True

def wyszukiwanieBinarne(T,a,n):
    l = 0
    p = n-1
    while l < p:
        srodek = (l+p)//2
        if a > T[srodek]:
            l = srodek + 1
        else:
            p = srodek
    return T[l] == a



# Zadanie 1
# for i in range(0, 10):
#     T.append(int(input("Podaj liczbę do tablicy: ")))
#
# n = len(T)
#
# if czyNiemalejaca(T) == False:
#     print("Podałeś nieposortowaną tablice")
#     exit()
#
# a = int(input("Podaj liczbę szukaną: "))
#
# if wyszukiwanieBinarne(T,a,n) == a:
#     print("Tak")
# else:
#     print("Nie")


# Zadanie 2
# T = []
def wyszukiwanieBinarneReku(T, a, lewy, prawy):
    if lewy < prawy:
        srodek = (lewy + prawy) // 2
        if a > T[srodek]:
            return wyszukiwanieBinarneReku(T,a,srodek+1, prawy)
        else:
            return wyszukiwanieBinarneReku(T,a,lewy, srodek)
    return T[lewy] == a

# for i in range(0, 5):
#     T.append(int(input("Podaj liczbę do tablicy: ")))
#
# if czyNiemalejaca(T) == False:
#     print("Podałeś nieposortowaną tablice")
#     exit()
#
# a = int(input("Podaj liczbę szukaną: "))
#
# if wyszukiwanieBinarneReku(T,a,0,len(T)-1):
#     print("Tak")
# else:
#     print("Nie")

# Zadanie 3
# plik = open("ciagi.txt")
# ciagi = plik.read().split("\n")
# plik.close()
#
# for i in range(0,len(ciagi)-1):
#     ciag = list(map(int, ciagi[i].split()))
#     if wyszukiwanieBinarne(ciag,10,len(ciag)-1):
#         print(ciag)


# Zadanie 4
# plik = open("ciagi2.txt")
# ciagi = plik.read().split("\n")
# plik.close()
#
# for i in range(1,len(ciagi)-1):
#     if i % 2 == 0:
#         ciag = list(map(int, ciagi[i].split()))
#         if wyszukiwanieBinarne(ciag, 10, len(ciag)):
#             print(ciag)


# Zadanie 4 v2 (optymalnie)
# plik = open("ciagi2.txt","r")
#
# n = int(plik.readline().rstrip())
#
# for i in range(n):
#     d = int(plik.readline().rstrip())
#     ciag = list(map(int, plik.readline().split()))
#     if wyszukiwanieBinarne(ciag,10,d):
#         print(ciag)
#
# plik.close()


# Zadanie 5

# funkcja wyszukiwanie_binarne(T, a, n):
#   lewy ← 1
#   prawy ← n
#   dopóki lewy < prawy wykonuj:
#       srodek ← (lewy + prawy) div 2
#       jeżeli T[srodek] < a to:
#           lewy ← srodek +1
#       w przeciwnym wypadku:
#           prawy ← srodek
#   zwróć T[lewy] = a i zakończ

#
# def wyszukiwanieBinarneZ5(T,a,n):
#     l = 1
#     p = n
#     while l < p:
#         srodek = (l+p)//2
#         if a > T[srodek]:
#             l = srodek + 1
#         else:
#             p = srodek
#     return T[l] == a
#
# for i in range(0, 10):
#     T.append(int(input("Podaj liczbę do tablicy: ")))
#
# T.insert(0,0)
# n = len(T)
#
# if czyNiemalejaca(T) == False:
#     print("Podałeś nieposortowaną tablice")
#     exit()
#
# a = int(input("Podaj liczbę szukaną: "))
#
# if wyszukiwanieBinarne(T,a,n) == a:
#     print("Tak")
# else:
#     print("Nie")

# Zadanie 6
from random import randint
T = []

T.append(randint(1,10))
for i in range(0,1000000):
    ostatnia = T[i]
    T.append(ostatnia+randint(1,3))

l = 0
p = len(T)-1
a = 1500000
ile = 0
jest = False
while l < p:
    srodek = (l+p)//2
    if a > T[srodek]:
        l = srodek + 1
        ile += 1
    else:
        p = srodek
        ile += 1
if T[l] == a:
    jest = True


plik = open("zadanie4.txt","w")
if jest:
    plik.write("tak ")
    plik.write(str(ile))
else:
    plik.write("nie ")
    plik.write(str(ile))

# Zadanie 7
# n = 10
# A = [0,5,99,3,7,111,13,4,24,4,8]
# i = 1
# while i<=n:
#     if A[i] % 2 == 0:
#         w = A[i]
#         break
#     i = i + 1
# print(w)
