# Faktoryzacja i dzielniki liczb – powtórzenie
# Link do zadań: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4

# 1. Napisz program, który wyświetli ile jest liczb pierwszych w pliku liczby1.txt.
# Odp. 4

# plik = open("liczby1.txt")
# liczby = list(map(int, plik.read().split()))
# plik.close()
# def CzyPierwsza(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
#
# ile = 0
# for i in liczby:
#     if CzyPierwsza(i):
#         ile += 1
# print(ile)

# 2. Napisz program, który wyświetli w osobnych wierszach te liczby z pliku liczby2.txt, które są
# podzielne przez 2.
# Odp.
# 32
# 36
# 38
# 52

# plik = open("liczby2.txt", "r")
# liczby = list(map(int, plik.read().split()))
# plik.close()
#
# for i in liczby:
#     if i % 2 == 0:
#         print(i)


# 3. Napisz program, który wyświetli łączną liczbę wszystkich dzielników właściwych liczb w pliku
# liczby2.txt
# Odp. 24

# def LiczbaDzielnikowWlasciwych(n):
#     ile = 0
#     for i in range(1,n):
#         if n % i == 0:
#             ile += 1
#     return ile
#
# plik = open("liczby2.txt", "r")
# liczby = list(map(int , plik.read().split()))
# plik.close()
#
# suma = 0
# for i in liczby:
#     suma += LiczbaDzielnikowWlasciwych(i)
# print(suma)


# 4. Napisz program, który wyświetli liczbę z pliku liczby2.txt, która ma największą sumę
# dzielników pierwszych. Jest tylko jedna taka liczba.
# Odp. 38

# plik = open("liczby2.txt")
# liczby = list(map(int, plik.read().split()))
# plik.close()
#
# def CzyPierwsza(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
#
# def SumaDzielnikowPierwszych(n):
#     suma = 0
#     for i in range(1,n):
#         if n % i == 0 and CzyPierwsza(i):
#             suma += i
#     return suma
#
# najwiekszaSumaDzielnikowPierwszych =  SumaDzielnikowPierwszych(liczby[0])
# indeks = 0
# for i in range(0, len(liczby)):
#     if SumaDzielnikowPierwszych(liczby[i]) > najwiekszaSumaDzielnikowPierwszych:
#         najwiekszaSumaDzielnikowPierwszych = SumaDzielnikowPierwszych(liczby[i])
#         indeks = i
# print(liczby[indeks])


# 5. Napisz program, który wyświetli liczby z pliku liczby2.txt, które mają najmniejszą sumę
# czynników pierwszych.

# plik = open("liczby2.txt")
# liczby = list(map(int, plik.read().split()))
# plik.close()
#
#
# def sumaCzynnikowPierwszych(n):
#     suma = 0
#     czynnik = 2
#     while n > 1:
#         while n % czynnik == 0:
#             suma += czynnik
#             n //= czynnik
#         czynnik += 1
#     return suma
#
# sumyCzynnikow = []
# for i in liczby:
#     sumyCzynnikow.append(sumaCzynnikowPierwszych(i))
#
# mini = min(sumyCzynnikow)
#
# for i in liczby:
#     if sumaCzynnikowPierwszych(i) == mini:
#         print(i)

# 6. Napisz program, który wyświetli w osobnych wierszach te liczby z pliku liczby2.txt, które mają co najmniej 2 różne czynniki pierwsze w rozkładzie na czynniki pierwsze.
# Odp.
# 21
# 36
# 38
# 52

# def liczbaRoznychCzynnikowPierwszych(n):
#     ile = 0
#     czynnik = 2
#     while n > 1:
#         while n % czynnik == 0:
#             n //= czynnik
#         czynnik += 1
#         ile += 1
#     return ile
#
# plik = open("liczby2.txt")
# liczby = list(map(int, plik.read().split()))
# plik.close()
#
# for i in liczby:
#     if liczbaRoznychCzynnikowPierwszych(i) >= 2:
#         print(i)

# 7. Napisz program, który wyświetli liczbę z pliku liczby2.txt, która ma najmniejszą sumę cyfr wszystkich czynników pierwszych. Jest tylko jedna taka liczba.
# 52

# def SumaCyfr(n):
#     suma = 0
#     while n > 0:
#         suma += n % 10
#         n //= 10
#     return suma
#
# def SumaCyfrCzynnikowPierwszych(n):
#     sumaCyfr = 0
#     czynnik = 2
#     while n > 1:
#         while n % czynnik == 0:
#             sumaCyfr += SumaCyfr(czynnik)
#             n //= czynnik
#         czynnik += 1
#     return sumaCyfr
#
# plik = open("liczby2.txt")
# liczby = list(map(int, plik.read().split()))
# plik.close()
#
# mini = SumaCyfrCzynnikowPierwszych(liczby[0])
# indeks = 0
#
# for i in range(0, len(liczby)):
#     if mini > SumaCyfrCzynnikowPierwszych(liczby[i]):
#         mini = SumaCyfrCzynnikowPierwszych(liczby[i])
#         indeks = i
#
# print(liczby[indeks])