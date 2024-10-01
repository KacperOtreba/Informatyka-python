# Badanie podzielności. Dzielniki liczb. Dzielniki pierwsze.
# Link do zadań: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4


# Zadanie 1 
#   Napisz program, który sprawdzi, czy liczba całkowita dodatnia n podana przez 
#   użytkownika dzieli się przez 2 i wyświetli jeden z komunikatów „Tak”, „Nie”.

# n = int(input())

# if n % 2 == 0:
#     print("Tak")
# else:
#     print("Nie")



# Zadanie 2
#   Napisz program, który wyświetli dzielniki liczby całkowitej dodatniej n podanej przez użytkownika.

# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)



# Zadanie 3
#   Napisz program, który wyświetli sumę dzielników liczby całkowitej dodatniej n podanej przez użytkownika.

# suma = 0
# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         suma += i

# print(suma)



# Zadanie 4
#   Napisz program, który wyświetli ile dzielników ma liczba całkowita dodatnia n podana przez użytkownika.

# ile = 0
# n = int(input())

# for i in range(1,n+1):
#     if n % i == 0:
#         ile += 1
# print(ile)



# Zadanie 5
#   Napisz program, który wyświetli dzielniki pierwsze liczby całkowitej dodatniej n podanej przez użytkownika.
#   Wskazówka:
#   Dzielnik pierwszy to taki dzielnik, który jest liczbą pierwszą.
def CzyPierwsza(n):
    ile = 0
    for i in range(2,n):
        if n % i == 0:    
            ile += 1
    if ile == 0:
        return True

# n = int(input())

# for i in range(1,n+1):
#     if n % i == 0 and CzyPierwsza(i) == True:
#         print(i)


# Zadanie 6
#   Napisz program, który sprawdzi, czy liczby całkowite dodatnie a i b podane przez użytkownika są liczbami bliźniaczymi. 
#   Liczby całkowite dodatnie są liczbami bliźniaczymi,  jeżeli są liczbami pierwszymi i ich różnica wynosi 2, 
#   np. liczby 5 i 7 oraz 11 i 13 są liczbami bliźniaczymi, a 7 i 9 nie są bliźniacze, bo 9 nie jest liczbą pierwszą.

# a = int(input("Podaj liczbę a: "))
# b = int(input("Podaj liczbę b: "))
#
# if CzyPierwsza(a) == True and CzyPierwsza(b) == True and abs(a - b) == 2:
#     print("Te liczby są bliźniacze")
# else:
#     print("Te liczby nie są bliźniacze")


# Zadanie 6v2
#   Znajdź liczby bliźniacze w przedziale 0-1000
#
# for i in range(1,100):
#     for j in range(1,100):
#         if CzyPierwsza(i) == True and CzyPierwsza(j) == True and abs(i-j) == 2:
#             print(F"Para {i}, {j}")


# Zadanie 7
#   Napisz program, który sprawdzi, czy liczba całkowita dodatnia n podana przez użytkownika jest liczbą
#   doskonałą. Liczba doskonała, to taka, która jest równa sumie swoich dzielników właściwych (czyli
#   mniejszych od tej liczby). Program wyświetli jeden z komunikatów „tak” lub „nie”. Przykładowe liczby
#   doskonałe:  6 = 1+2+3 ;  28 = 1+2+4+7+14

# n = int(input("Podaj dodatnią liczbę całkowitą: "))
#
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum += i
#
# if sum == n:
#     print("TAK")
# else:
#     print("NIE")


# Zadanie 8
#   Napisz program, który sprawdzi, czy liczby całkowite dodatnie a i b podane przez użytkownika są
#   liczbami zaprzyjaźnionymi. Liczby całkowite dodatnie a i b są liczbami zaprzyjaźnionymi, jeżeli są
#   różne oraz suma dzielników właściwych liczby a jest równa liczbie b oraz suma dzielników właściwych
#   liczby b jest równa liczbie a. Program wyświetli jeden z komunikatów „tak” lub „nie”. Przykłady liczb
#   zaprzyjaźnionych:
#   Dzielniki liczby 284: 1, 2, 4, 71, 142
#   Dzielniki liczby 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
#   220 = 1 + 2 + 4 + 71 + 142
#   284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110
#   Kolejna para liczb zaprzyjaźnionych: 1184 i 1210

def SumaDzielWłaść(n):
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    return suma


# a = int(input("Podaj liczbę a: "))
# b = int(input("Podaj liczbę b: "))
#
# if a != b and a == SumaDzielWłaść(b) and b == SumaDzielWłaść(a):
#     print("TAK")
# else:
#     print("NIE")


# Zadanie 8v2

for i in range(1,1000):
    for j in range(1,1000):
        if i != j and i == SumaDzielWłaść(j) and j == SumaDzielWłaść(i):
            print(f"Para: {i}, {j}")



