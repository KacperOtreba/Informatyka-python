# Badanie podzielności. Dzielniki liczb. Dzielniki pierwsze.


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

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

if CzyPierwsza(a) == True and CzyPierwsza(b) == True and abs(a - b) == 2:
    print("Te liczby są bliźniacze")
else:
    print("Te liczby nie są bliźniacze")