# 09. Znajdowanie podciągów o różnych własnościach
# Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4

# Zadanie 1
print("Zadanie 1")

plik = open("liczby.txt", "r")
liczby = list(map(int, plik.readline().rstrip().split()))
plik.close()

for i in range(1, len(liczby) + 1):
    for j in range(0, len(liczby) - i + 1):
        print(*liczby[j:i + j])

# Zadanie 2
print("Zadanie 2")

plik = open("liczby.txt", "r")
liczby = list(map(int, plik.readline().rstrip().split()))
plik.close()

for i in range(len(liczby)):  # i to index początkowy
    for j in range(1, len(liczby) - i + 1):  # j to długość
        print(*liczby[i:i + j])  # i + j to index końcowy

# Zadanie 3
print("Zadanie 3")

plik = open("liczby.txt", "r")
liczby = list(map(int, plik.readline().rstrip().split()))
plik.close()

for i in range(len(liczby) - 4):
    suma = 0
    suma = sum(liczby[i:i + 5])
    print(liczby[i:i + 5], suma)

# Zadanie 4
print("Zadanie 4")

plik = open("liczby.txt", "r")
liczby = list(map(int, plik.readline().rstrip().split()))
plik.close()

for i in range(len(liczby)):  # i to index początkowy
    for j in range(3, len(liczby) - i + 1):  # j to długość
        print(*liczby[i:i + j])  # i + j to index końcowy

# Zadanie 6
print("Zadanie 6")


def Czy_Rosnaca(T):
    for i in range(0, len(T) - 1):
        if T[i] >= T[i + 1]:
            return False
    return True


liczby = input("Podaj ciąg liczb: ")
liczby = list(map(int, liczby.split()))

if Czy_Rosnaca(liczby):
    print("tak")
else:
    print("nie")

# Zadanie 7
print("Zadanie 7")


def Czy_Malejacy(T):
    for i in range(0, len(T) - 1):
        if T[i] <= T[i + 1]:
            return False
    return True


liczby = input("Podaj ciąg liczb: ")
liczby = list(map(int, liczby.split()))

if Czy_Malejacy(liczby):
    print("tak")
else:
    print("nie")

# Zadnie 8
print("Zadanie 8")


def Czy_Nierosnacy(T):
    for i in range(0, len(T) - 1):
        if T[i] < T[i + 1]:
            return False
    return True


liczby = input("Podaj ciąg liczb: ")
liczby = list(map(int, liczby.split()))

if Czy_Nierosnacy(liczby):
    print("tak")
else:
    print("nie")

# Zadanie 9
print("Zadanie 9")


def Czy_Niemalejacy(T):
    for i in range(0, len(T) - 1):
        if T[i] > T[i + 1]:
            return False
    return True


liczby = input("Podaj ciąg liczb: ")
liczby = list(map(int, liczby.split()))

if Czy_Niemalejacy(liczby):
    print("tak")
else:
    print("nie")

# Zadanie 10
print("Zadanie 10")


def Czy_Staly(T):
    for i in range(0, len(T) - 1):
        if T[i] != T[i + 1]:
            return False
        return True


liczby = input("Podaj ciąg liczb: ")
liczby = list(map(int, liczby.split()))

if Czy_Staly(liczby):
    print("tak")
else:
    print("nie")

# Zadanie 11
print("Zadanie 11")

# Złożoność kwadraowa
# def d_Niemalejacego(T):
#     for i in range(0,len(T)-1):
#         if T[i] > T[i+1]:
#             return i+1
#     return len(T)
#
# plik = open("liczby.txt", "r")
# liczby = list(map(int, plik.readline().rstrip().split()))
# plik.close()
#
# dlugosci = []
#
# for i in range(len(liczby)):
#     temp = d_Niemalejacego(liczby[i:])
#     dlugosci.append(temp)
#
# print(max(dlugosci))

plik = open("liczby.txt", "r")
liczby = list(map(int, plik.readline().rstrip().split()))
plik.close()

aktualna_dlugosc = 1
maks_dlugosc = 1
n = len(liczby)
for i in range(1,n):
    if liczby[i]>=liczby[i-1]:
        aktualna_dlugosc += 1
        if aktualna_dlugosc > maks_dlugosc:
            maks_dlugosc = aktualna_dlugosc
    else:
        aktualna_dlugosc = 1
print(maks_dlugosc)


# Zadanie 12
print("Zadanie 12")

plik = open("liczby.txt", "r")
liczby = list(map(int, plik.readline().rstrip().split()))
plik.close()

pocz_index = 0
kon_index = 0
n = len(liczby)
for i in range(1,n):
    if len(liczby[pocz_index:kon_index]) == maks_dlugosc:
        print(liczby[pocz_index:kon_index])
        break
    if liczby[i]>=liczby[i-1]:
        kon_index += 1
    else:
        pocz_index = i
        kon_index = i + 1


# Zadanie maturalne
print("Zadanie maturalne")

folder = "zadanie maturalne 1/pi_przyklad.txt"
plik = open(folder)
liczby = list(map(int, plik.read().rstrip().split()))
plik.close()

dwujki = []
for i in range(len(liczby) - 2):
    dwujki.append(liczby[i:i + 2])

ile = 0
for i in dwujki:
    if i > 90:
        ile += 1
print(ile)