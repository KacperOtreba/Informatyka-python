# print("Zadanie 1")
# a = int(input("FIRST: "))
# b = int(input("SECOND: "))
# c = int(input("THIRD: "))

# if a - b == b - c:
#   print("Arytmetyczny")

# if a / b == b / c:
#   print("Geometryczny")

# if a < b < c:
#   print("Rosnący")

# if a > b > c:
#   print("Malejący")

# print("Zadanie 2")
# suma = 0
# for i in range(100,1000):
#   if i % 8 == 0 and i % 16 != 0:
#     suma += i

# print(suma)

# print("Zadanie 3")
# ilosc = 0
# najw = 0
# for i in range(10,100):
#   if i > najw and i % 7 == 0:
#     najw = i

# for x in range(1000,100000):
#   if x % najw == 0:
#     ilosc += 1

# print(ilosc)

# print("Zadanie 4")
# ilosc = 0
# for i in range(10,100):
#   if i / 10 > i % 10 * 2:
#     ilosc += 1
# print(ilosc)

# print("Zadanie 5")
# suma = 0
# ilosc = 0
# for i in range(100,10000):
#   if i / 100 > (i % 100 / 10) + (i % 10):
#     suma += i
#     ilosc += 1
# print(f"suma to: {suma}")
# print(f"ilosc to: {ilosc}")

# print("Zadanie 6")
# n = int(input())
# suma = 0
# ilosc = 0
# for i in range(10, 100):
#   if i % 19 == 0:
#     suma += i
#     ilosc += 1
#   if n == ilosc:
#     print(suma)
#     break
#   if i == 99:
#     print("Out of range")

# print("Zadanie 7")
# suma = 0
# ilosc = 0
# n = int(input())
# for i in range(999,100,-1):
#   if i % 37 == 0:
#     suma += i
#     ilosc += 1
#   if n == ilosc:
#     print(suma)
#     break
#   if i == 99:
#     print("OUT OF RANGE")

# print("Zadanie 8")
# n = int(input("Ile powtorzen chcesz: "))
# suma = 0
# rytm = 2
# for i in range(n):
#   if i % 2 != 0:
#     rytm *= -1
#     suma += rytm
#     rytm *= -1
#   else:
#     suma += rytm
#   rytm += 3
# print(suma)

# print("Zadanie 9")
# n = int(input("Ile powtorzeń: "))
# iloczyn = 1
# rytm = 2
# for i in range(2, n+2):
#     rytm *= 2
#     if i % 2 == 0:
#         rytm *= -1
#         iloczyn *= rytm
#         rytm *= -1
#     else:
#         iloczyn *= rytm
# print(iloczyn)


# print("Zadanie 10")
# n = int(input("Jak dlugi:"))
# suma = 0
# silnia = 1
# rytm = 1
# for i in range(n):
#     iloczyn += silnia
#     silnia *= rytm
#     rytm += 1

# print(suma)


# print("Zadanie 11")
# n = int(input("Jak dlugi: "))
# suma = 0
# licznik = 1
# mianownik = 1
# for i in range(n):
#     suma += licznik / mianownik
#     licznik += 2
#     mianownik += licznik

# print(suma)


# print("Zadanie 12")
# n = int(input("Jak dlugi: "))
# licznik = 0
# mianownik = 0
# ciag1 = 1
# ciag2 = 1
# for i in range(n):
#     licznik += ciag1
#     mianownik += ciag2
#     ciag1 += 2
#     ciag2 += ciag1

# print(licznik/mianownik)


# print("Zadanie 13")
# n = int(input("Jak dlugi: "))
# suma = 0
# licznik = 2
# mianownik = 3
# for i in range(2, n+2):
#     suma += licznik / mianownik
#     licznik += 2
#     mianownik = (i**3)+2

# print(suma)


# print("Zadanie 15")
# licznik = 1
# mianownik = 1
# ciag1 = 3
# ciag2 = 1
# for i in range(n):
#     licznik *= ciag1
#     mianownik *= ciag2
#     ciag1 += 1
#     ciag2 = (ciag2*2)+1

# print(licznik / mianownik)


# print("Zadanie 16")
# n = int(input("Jak dlugi: "))
# licznik = 1
# mianownik = 1
# ciag1 = 1
# ciag2 = 1
# fib1 = 1
# fib2 = 1
# sumafib = 0
# for i in range(n):
#     licznik *= ciag1
#     mianownik *= ciag2
#     sumafib = fib1 + fib2
#     fib1 = fib2
#     fib2 = sumafib
#     ciag1 = sumafib
#     ciag2 *= 2

# print(licznik / mianownik)