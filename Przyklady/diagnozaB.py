from math import gcd
from math import lcm
# Diagnoza INF

# - WSTĘP
# 1. Oblicz sumę liczb 3-cyfrowych
# print("Wstęp-Zadanie 1")
# suma = 0
# for i in range(100,1000):
#     suma += i
# print(suma)

# 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
# print("Wstęp-Zadanie 2")
# suma = 0
# ilosc = 0
# for i in range(10,100):
#     if i % 6 == 0:
#         suma += i
#         ilosc += 1
# print(suma)
# print(ilosc)

# 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
# from random import randint
# liczby = []
# for i in range(5): liczby.append(randint(1000,10000))
# print(liczby)
# print(max(liczby))

# 4. Podaj sumę cyfr w dowolnej liczbie
# liczba = input()
# suma = 0
# for i in liczba:
#     suma += int(i)
# print(suma)

# 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
# liczba = input()
# mini = liczba[0]
# for i in liczba:
#     if i < mini:
#         mini = i
# print(mini)

# - ALGORYTMY
# 1. Sprawdź czy wpisana przez usera liczba jest pierwsza
# def CzyPierwsza(x):
#     for i in range(2,x):
#         if x % i:
#             return False
#         else:
#             return True

# if CzyPierwsza():
#     print("NIE")
# else:
#     print("TAK")
# 2. Sprawdź czy wpisana przez usera liczba jest złożona
# def CzyZlozona(x):
#     dziel = 0
#     for i in range(2,x):
#         if x % i == 0:
#             dziel += 1
#     if dziel > 0:
#         return True

# if CzyZlozona(11):
#     print("Jest złożona")
# else:
#     print("Nie jest złożona")
# 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24
# a = int(input())
# b = 24
# if gcd(a,b) == 1:
#     print("Tak jest względnie pierwsza")
# else:
#     print("Nie jest względnie pierwsza")
# 4. Zakoduj szyfrem CEZARA i kluczem k słowo s.
# napis = input("Podaj napis a ja go zaszyfruje: ")
# szyfr = ""
# klucz = int(input())
# for i in range(len(napis)):
#     szyfr += chr((ord(napis[i]) - 65 + klucz) % 26 + 65)
# print(szyfr)

# 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.
licznik1 = int(input("Licznik1: "))
mianownik1 = int(input("Mianownik1: "))
licznik2 = int(input("Licznik2: "))
mianownik2 = int(input("Mianownik2: "))


wspolnyMianownik = lcm(mianownik1, mianownik2)

gotowyLicznik1 = (wspolnyMianownik // mianownik1) * licznik1
gotowyLicznik2 = (wspolnyMianownik // mianownik2) * licznik2

dodanyLicznik = gotowyLicznik1 + gotowyLicznik2

dzielnik = gcd(dodanyLicznik, wspolnyMianownik)
licznik = dodanyLicznik // dzielnik
mianownik = wspolnyMianownik // dzielnik

print(f"Ulamek nieskracalny: {licznik} / {mianownik}")
if licznik % mianownik == 0:
    print(f"Calosci: {licznik // mianownik}")
else:
    print(f"Calosci: {licznik // mianownik} i {licznik % mianownik} / {wspolnyMianownik}")

# 6. Znajdź NWW dwóch wpisanych przez usera liczb
# a = int(input())
# b = int(input())
# print(lcm(a,b))

# - KARTKA
# 1. Oblicz wartość ONP - 8822+/234*---
# 2. Znajdź postać ONP dla pisanego wyrażenia - (3+8)/4-6*(3*4/2)
# 3. Napisz na kartce algorytm NWD (obie wersje) i przeprowadz symulacje kroków dla podanych liczb - dowolny i a=35 b=56

# - NAPISY
# 1. Znajdź ilość liter C we wpisanym napisie
# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp
# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.