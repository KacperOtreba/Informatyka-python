# 04. Sito Eratostenesa
# Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4

# zadanie 1

# n = int(input("Podaj n: "))


def sito(n):
    czy_pierwsza = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if czy_pierwsza[p]:
            for i in range(p * p, n + 1, p):
                czy_pierwsza[i] = False
        p += 1
    return czy_pierwsza


# czy_pierwsza = sito(n)
#
# for i in range(2, len(czy_pierwsza)):
#     if czy_pierwsza[i]:
#         print(i)

# # zadanie 2
# print("Zadanie 2")
# ile = 0
# suma = 0
# for i in range(2, len(czy_pierwsza)):
#     if czy_pierwsza[i] and i <= n:
#         suma += i
#         ile += 1
#
# print(ile)
# print(suma)
#
# # zadanie 3
# print("Zadanie 3")
#
#
# def sitoZPetlaDopoki():
#     czy_pierwsza = [True] * (n + 1)
#     p = 2
#     temp = p * p
#     while p * p <= n:
#         if czy_pierwsza[p]:
#             while temp <= n:
#                 czy_pierwsza[i] = False
#             temp += n + 1
#         p += 1
#
#
# # czy_pierwsza[0] ← fałsz
# # czy_pierwsza[1] ← fałsz
# # dla i=2,3,...,n wykonuj
# #   czy_pierwsza[i] ← prawda
#
# # p ← 2
# # temp <- p * p
# # dopóki p * p ⩽ n wykonuj
# #   jeżeli czy_pierwsza[p] = prawda
# #       dopoki temp <= n
# #           czy_pierwsza[i] ← fałsz
# #       temp = temp + n + 1
# #    p ← p + 1
#
#
# zadanie 4
# czesc 1
# print("Zadane 4 czesc 1")
# n = 1000
# czy_pierwsza = sito(n)
#
# for i in range(2, len(czy_pierwsza)):
#     if czy_pierwsza[i]:
#         print(i)
#
# # czesc 2
#
# print("Zadanie 4 czesc 2")
# ile = 0
# file = open("liczby.txt", "r")
# for line in file:
#     if czy_pierwsza[int(line)]:
#         ile += 1
# print(ile)
# file.close()


# # zadanie 5
# print("Zadanie 5")
# a = int(input("Podaj liczbe a: "))
# b = int(input("Podaj liczbe b: "))
#
# ile = 0
# suma = 0
# czy_pierwsza = [True] * (b + 1)
# while a * a <= b:
#     if czy_pierwsza[a]:
#         for i in range(a * a, n + 1, a):
#             czy_pierwsza[i] = False
#     a += 1
#
# # zadanie 6