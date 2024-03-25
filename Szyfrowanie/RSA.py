#PRE
# from math import gcd
# print(gcd(12,16))

# 1. wybór 2 dużych liczb pierwszych
p = 409
q = 283


# # 2. Stworzenie funkcji F = (p-1) * (q-1)
F = (p-1) * (q-1)
n = q * p


# # 3. Znalezienie klucza publicznego e: NWD(F,e) = 1
from math import gcd
for i in range(2, F):
  if gcd(i,F) == 1:
    e = i
    break


# # 4. Wygenerowanie klucza prywatnego d: d*e mod F = 1 (odwrotność modulo)
d = 0
for i in range(3, n, 2):
  if (i*e) % F == 1:
    d = i
    break


# # Przykład działania kodowania znaku x:
# # c = x**c mod n (na szfrogram)
# # t = c**d mod n (na tekst jawny)

msg = input()
szyfrogram = ""


for i in msg:
  szyfrogram += chr((ord(i)**e) % n)


jawny = ""
for j in szyfrogram:
  jawny += chr((ord(j)**d)% n)
print(jawny)


p = 11
q = 13
F = (p-1) * (q-1)
n = p * q
from math import gcd
for i in range(2,F):
  if gcd(i, F) == 1:
    e = i
    break
for i in range(3,n,2):
  if (i*e) % F == 1:
    d = i
    break
msg = input()
szyfrogram = ""
jawny = ""
for i in msg:
  szyfrogram += chr((ord(i)**e) % n)
for i in szyfrogram:
  jawny += chr((ord(i)**d) % n)
print(szyfrogram)
print(jawny)

