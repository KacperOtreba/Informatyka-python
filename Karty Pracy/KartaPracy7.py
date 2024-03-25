from random import randint
T = []

for i in range(40):
  T.append(randint(10,99))

print(T)

# print("Zadanie 1")
# # 1
# print(max(T))
# # 2
# maks = T[0]
# for item in T:
#   if item > maks:
#     maks = item
# print(maks)

# print("Zadanie 2")
# # 1
# print(min(T))
# # 2
# mini = T[0]
# for item in T:
#   if item < mini:
#     mini = item
# print(mini)

# print("Zadanie 3")
# # 1
# print(len(T))
# # 2
# ilosc = 0
# for item in T:
#   ilosc += 1
# print(ilosc)

# print("Zadanie 4")
# # 1 NIE DA SIĘ
# # 2
# vcemaks = T[0]
# for item in T:
#   if item > vcemaks and item < max(T):
#     vcemaks = item
# print(max(T))
# print(vcemaks)

# print("Zadanie 5")
# 1 NIE DA SIĘ
# 2
# vcemini = T[0]
# for item in T:
#   if item < vcemini and item > min(T):
#     vcemini = item
# print(min(T))
# print(vcemini)

# print("Zadanie 6")
# # 1
# print(T.count(max(T)))
# 2 
# ilosc = 0
# for item in T:
#   if item == max(T):
#     ilosc += 1
# print(ilosc)

# print("Zadanie 7")
# # 1
# print(T.count(min(T)))
# # 2
# ilosc = 0
# for item in T:
#   if item == min(T):
#     ilosc += 1
# print(ilosc)

# print("Zadanie 8")
# # 1
# x = int(input("Podaj liczbę: "))
# print(T.count(x))
# # 2
# x = int(input("Podaj liczbę: "))
# ilosc = 0
# for item in T:
#   if x == item:
#     ilosc += 1
# print(ilosc)

# print("Zadanie 9")
# 1 NIE DA SIĘ
# 2
# suma = 0
# for item in T:
#   suma += item
# x = suma/40
# print(round(x,1))

# print("Zadanie 10")
# # 1 IDK
# # 2
# suma = 0
# for i in range(len(T)):
#   if i % 2 == 0:
#     suma += T[i]
# print(suma)

# print("Zadanie 11")
# # 1 IDK
# # 2
# suma = 0
# for i in range(len(T)):
#   if i % 2 != 0:
#     suma += T[i]
# suma /= 40
# print(suma)

# print("Zadanie 12")
# TO DO

# print("Zadanie 13")
# for i in range(10,100):
#   if i not in T:
#     print(i, end=" ")

print("Zadanie 14")
