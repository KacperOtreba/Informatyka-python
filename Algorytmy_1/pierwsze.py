# 1.Algorytm sprawdzający czy liczba jest pierwsza
# temp = 0
# n = int(input())
# for i in range(1,n+1):
#   if n % i == 0:
#     temp += 1
# if temp == 2:
#   print("Liczba jest pierwsza")
# else:
#   print("Liczba nie jest pierwsza")

# # pan by tak chciał
# from math import sqrt
# n = int(input())
# for i in range(2, int(sqrt(n)) + 1):
#   if n % i == 0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza")

# print()
# L = "2 100".split()
# print(L)

# generator liczb pierwszych

# p = int(input("Pocz tych liczb: "))
# q = int(input("Kon tych liczb: "))
# for i in range(p, q+1):
#   flaga = True
#   for j in range(2, int(i**0.5)+1):
#     if i % j == 0:
#       flaga = False
#   if flaga:
#       print(i, end=" ")


# n = int(input("Podaj ile chcesz liczb pierwszych: "))
# x = 2
# while 1:
#     flaga = True
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             flaga = False
#     if flaga:
#         print(x, end=" " )
#         n = n - 1
#         if n == 0:
#             break
#     x = x + 1


#przecwiczenie algorytmu spraw czy liczba jest pierwsza
# temp = 0
# n = int(input())
# for i in range(1,n+1):
#   if n % i == 0:
#     temp += 1
# if temp == 2:
#     print("Liczba jest pierwsza")
# else:
#     print("Liczba nie jest pierwsza")