# 08. Schemat hornera
# Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4

# Zadanie 2
print("Zadanie 2")

def Horner(A, n, x):
    y = A[n]
    for i in range(n-1, 0 ,-1):
        y = x * y + A[i]
    return y


wspolczynniki = input("Podaj współczynniki: ")
A = list(map(int, wspolczynniki.split()))


# Zadanie 6
print("Zadanie 6")
binarna = input("Podaj liczbę binarną: ")
#s1
# n = len(binarna)
# w = int(binarna[0])
# for i in range(1,n):
#     w = w*2+int(binarna[i])
# print(w)

#s2
w = 0
for cyfra in binarna:
    w = w * 2 + int(cyfra)
print(w)


# Zadanie 7
print("Zadanie 7")
p = input("Podaj podstawę: ")
liczba = input("Podaj liczbę w systemie o podstawie p: ")

w = 0
for cyfra in liczba:
    w = w * p + int(cyfra)
print(w)