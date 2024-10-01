# Faktoryzacja
# # Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4


# Zadanie 1
#   Napisz program, który wczyta liczbę naturalną n&gt;1 z klawiatury i wyświetli czynniki pierwsze liczby n
#   w osobnych liniach.
# n = int(input())
# czynnik = 2
# while n>1:
#     while n % czynnik == 0:
#         print(czynnik)
#         n = n / czynnik
#     czynnik += 1


# Zadanie 2
#   Napisz program, który wczyta liczbę naturalną n&gt;1 z klawiatury i wyświetli sumę czynników
#   pierwszych tej liczby.
# suma = 0
# n = int(input())
# czynnik = 2
# while n>1:
#     while n % czynnik == 0:
#         suma += czynnik
#         n = n / czynnik
#     czynnik += 1
# print(suma)


# Zadanie 3
#   Napisz program, który wczyta liczbę naturalną n>1 z klawiatury i wyświetli komunikat, czy suma
#   czynników pierwszych liczby n jest liczbą pierwszą.
def CzyPierwsza(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# n = int(input())
# czynnik = 2
# suma = 0
# while n>1:
#     while n % czynnik == 0:
#         suma += czynnik
#         n = n / czynnik
#     czynnik += 1
# if (CzyPierwsza(suma)):
#     print("tak")
# else:
#     print("nie")


# Zadanie 4
#   Napisz program, który wyświetli liczbę różnych czynników pierwszych liczby n podanej przez
#   użytkownika.

n = int(input())
czynnik = 2
T = []
ile = 0
while n>1:
    while n % czynnik == 0:
        if czynnik not in T:
            T.append(czynnik)
            ile += 1
        czynnik += 1
print(f"Liczba posiada {ile} róźnych czynników pierwszych")


# Zadanie 5
# Napisz program, który sprawdzi, czy liczba naturalna n>1 podana przez użytkownika jest liczbą
# Smitha.
# https://pl.wikipedia.org/wiki/Liczba_Smitha
# Wskazówka:
# Przykład: cyfry liczby 123
# 123 mod 10 = 3
# 123 div 10 = 12
# 12 mod 10 = 2
# 12 div 10 = 1
# 1 mod 10 = 1
# 1 div 10 = 0
# Algorytm, który oblicza sumę cyfr liczby dziesiętnej:
# Specyfikacja:
# Dane:
# n - liczba całkowita dodatnia
# Wyniki:
# suma cyfr liczby n w systemie dziesiętnym
# Algorytm (pseudokod):
# funkcja suma_cyfr(n):
# suma ← 0
# dopóki n>0 wykonuj
# reszta ← n mod 10
# suma ← suma + reszta
# n ← n div 10
# zwróć suma

def CzyZlozona(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return True
    return False

def SumaCyfr(n):
    suma = 0
    while n>0:
        suma += n % 10
        n = n // 10
    return suma


def SumaCyfrCzynnikow(n):
    czynnik = 2
    suma_cyfr_czynnikow = 0
    while n > 1 :
        while n % czynnik == 0:
            suma_cyfr_czynnikow += SumaCyfr(czynnik)
            n = n // czynnik
        czynnik += 1
    return suma_cyfr_czynnikow

n = int(input("Podaj liczbę: "))
sumaN = SumaCyfr(n)


if CzyZlozona(n) == True and sumaN == SumaCyfrCzynnikow(n):
    print("tak")
else:
    print("nie")