# print("Zadanie 1")
# n = int(input("Podaj liczbe: "))
# wynik = 0
# while n > 0:
#   wynik += n % 10
#   n = n // 10
# print("Suma cyfr tej liczby to: ", wynik)

# print("Zadanie 2")
# n = int(input())
# dzielniki = 0
# for i in range(1, n+1):
#   if n % i == 0:
#     dzielniki += 1
# if dzielniki == 2:
#   print("TAK")
# else:
#   print("NIE")

# print("Zadanie 3")
# n = int(input("Podaj liczbe: "))
# suma = 0
# for i in range(1,n):
#   if n % i == 0:
#     suma += i
# if suma == n:
#   print("Liczba jest doskonała")
# else:
#   print("Liczba nie jest doskonała")

# print("Zadanie 4")
# a = int(input("Podaj 1 liczbe: "))
# b = int(input("Podaj 2 liczbe: "))
# while b > 0:
#   a, b = b, a % b
# nwd = a
# if nwd == 1:
#   print("Liczby są względnie pierwsze")
# else:
#   print("Liczby nie są względnie pierwsze")

# print("Zadanie 5")
# n = int(input())
# for i in range(10,20):
#   x = n
#   y = i
#   while y > 0:
#     x, y = y, x % y
#   nwd = x 
#   if nwd == 1:
#     print(n,i)

# print("Zadanie 6")
# a = int(input("Podaj licznik: "))
# b = int(input("Podaj mianownik: "))
# x = a
# y = b
# while y > 0:
#   x, y = y, x % y
# nwd = x
# print(a // nwd)
# print("---")
# print(b // nwd)

# print("Zadanie 7")
# a = int(input("Podaj licznik: "))
# b = int(input("Podaj mianownik: "))
# liczba = 0
# X = a
# Y = b
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# X = X // a
# Y = Y // b

# if X >= Y:
#     liczba = X // Y
#     X -= Y * liczba
# print(f"{liczba} i {X}/{Y}")

# print("Zadanie 8")
# T = []
# for i in range(2,1000001):
#   suma1 = 0
#   for j in range(1,i):
#     if i % j == 0:
#       suma1 += j
#   T.append(suma1)
#   suma2 = 0
#   for k in range(1,suma1):
#     if suma1 % k == 0:
#       suma2 += k
#   if i == suma2 and suma1 != suma2 and suma2 not in T:
#     print(f"({suma1}, {suma2})")

# print("Zadanie 9")
# def czy_pierwsza(n):
#   for i in range(2,n):
#     if n % i == 0:
#       return False
#   return True

# print("Zadanie 10")

