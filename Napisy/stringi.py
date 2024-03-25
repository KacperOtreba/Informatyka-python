# * Operacje na stringach (napisach)
# string to jakby "lista"; zachowuje sie jak lista
s = input()

for x in s:
    print(x)

print()

for x in range(len(s)):
    print(s[x])

# Zamienianie napisu na liste i posortowac
L = list(s)
L.sort()
print(L)

# laczy liste w jeden napis a "" jest tym co je moze laczyc
w = "".join(L)
print(w)
# * jak sprawdzic czy wyraz jest palindrom

cos = input()
odwrocone = list(cos)
odwrocone.reverse()
czy = "".join(odwrocone)
if cos == czy:
    print("tak")
else:
    print("nie")


# * Szukanie palindromow w tablicy (Tutaj tablica jako napis jest)
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        print("Nie") # Zamiast printow moga byc exity ale to w innych przydkach
print("Tak")

print()
# * Jak sprawdic czy liczba jest anagramem - szukanie sortowaniem
a, b = input(), input()
X, Y = list(a), list(b)

X.sort()
Y.sort()
a, b = "".join(X), "".join(Y)

if a == b:
    print("tak")
else:
    print("nie")

print()
# * Szukanie anagramu w tablicy - Produkuje liste z kodami ASCII i pozniej sprawdza czy na danych pozycjach od slow znajduje sie to samo
a, b = input(), input()
X, Y = [0] * 150, [0] * 150

for i in range(len(a)):
    X[ord(a[i])] += 1

for i in range(len(b)):
    Y[ord(b[i])] += 1
print(X)

if X == Y:
    print("tak")
else:
    print("nie")