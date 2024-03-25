# program dodający 2 ułamki
a = int(input("Podaj licznik pierwszego ułamka: "))
b = int(input("Podaj mianownik pierwszego ułamka: "))

c = int(input("Podaj licznik drugiego ułamka: "))
d = int(input("Podaj mianownik drugiego ułamka: "))
x = b
y = d
temp = x * y
while y > 0:
  x, y = y, x % y
# print(temp // b)
nww = temp // x
g = (nww // b) * a
h = (nww // b) * c
i = g + h
print(f"{a}/{b} + {c}/{d} = {g}/{nww} + {h}/{nww} = {i}/{nww}")
print("", i)
print("----")
print("", nww)