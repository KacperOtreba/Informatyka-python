# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
# a = input()
# print(a[0], a[-1])


# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
# a = input()
# print(a[1:-1])


# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca
# a = input()
# print(a[:-5:-1])


# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis
# a = input()
# s = 0
# for i in a:
#     s += ord(i)
# print(s)


# 5. Policz ile we wpisanym napisie jest liter A.
# a = input()
# suma = 0
# for i in a:
#     if i == "A":
#         suma += 1
# print(suma)


# 6. Podaj dominującą literkę we wpisanym napisie. 
# Niech to będzie tylko jedna literka.
# a = input()
# b = list(a)
# maksik = 0
# for i in b:
#     spr = b.count(i)
#     if spr > maksik:
#         maksik = spr
#         literka = i
# print(literka)


# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)
# def czyJestMniejszyNiezerowy(L, n):
#     for x in L:
#         if 0 < L.count(x) < n:
#             return True
#         return False

# napis = input()
# K = [0] * 100
# for x in napis:
#     K[ord(x)] += 1
# print(K)
# domikand = max(K)

# if sum(K) == max(K):
#     print("Dominanta:" , chr(K.index(max(K))))
# elif not czyJestMniejszyNiezerowy(K):
#     print("Brak dominanty")
# else:
#     D = []
#     for i in range(len(K)):
#         if K[i] == max(K):
#             D.append(chr(i))
#     print("Dominanty:", " ".join(D))


# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
# napis = input()
# ilopodc = 0
# for i in range(len(napis)):
#     if napis[i] == "L" and napis[i+1] == "A":
#         ilopodc += 1
# if ilopodc == 3:
#     print("TAK")
# else:
#     print("NIE")


# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)
# napis = input()
# suma = 0
# for i in range(len(napis)):
#     suma += ord(napis[i])
# sred = suma // len(napis)
# print(f"Średnia literka tego napisu to: {chr(sred)}")


# 10. Wypisz literki, których nie ma w napisie
# napis = input()
# ASCII = []
# for i in range(65,91):
#     ASCII.append(i)

# for i in range(len(napis)):
#     ASCII.remove(ord(napis[i]))

# for i in ASCII:
#     print(chr(i), end=" ")


# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)