# 06. Przetwarzanie plików oraz operacje na napisach
# Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4

# Przyklad 1
# Program, który odczytuje słowa zapisane w pliku slowa.txt i wyświetla je wraz z informacją o liczbie liter każdego
# słowa

# plik = open("slowa.txt","r")
# for linia in plik :
#     linia.strip()
#     print(linia, len(linia))
# plik.close()
#
#
#
# Przyklad 2
# Program, który zapisuje w pliku nowy.txt liczby od 1 do 10.
#
# plik = open('nowy.txt',"w")
# for i in range(1,11):
#     plik.write(str(i)+"\n")
# plik.close()
#
#
# Przyklad 3
# Program, który kopiuje słowa zawarte w pliku slowa.txt do pliku slowa_numerowane.txt doklejając kolejne numery
# słów (zaczynając od 1) na początku każdej linii.
#
# plikA = open('slowa.txt','r')
# plikB = open('slowa_numerowane.txt','w')
# numer = 0
# for linia in plikA:
#     numer += 1
#     plikB.write(f"{numer}: {linia}")
# plikA.close()
# plikB.close()
#
#
# Przyklad 4
# Program, który liczy ilość słów w pliku slowa.txt.

# with open('slowa.txt','r') as plik:
#     print(len(plik.readlines()))


# Przyklad 5
# Program, który odczyta z pliku liczby_w_linii.txt linię tekstu zawierającą liczby rozdzielone spacją oraz wyświetli sumę
# tych liczb.

# plik = open('liczby_w_linii.txt', 'r')
# linia = plik.readline()
# liczby = list(map(int,linia.rstrip().split()))
# print(sum(liczby))


# Zadanie 1
# Napisz program, który zapyta użytkownika o podanie imienia i nazwiska, a następnie zapisze te dane w pliku
# dane_osobowe.txt w dwóch wierszach (pierwszy wiersz imię, drugi nazwisko).

# firstname = input("Podaj imie: ")
# lastname = input("Podaj nazwisko: ")
#
# plik = open('dane_osobowe.txt', 'w')
# plik.write(firstname + "\n" + lastname)
# plik.close()


# Zadanie 2
# Napisz program, który odczyta imię i nazwisko zapisane w pliku dane_osobowe.txt i wyświetli powitanie
# „Witaj imię i nazwisko”, gdzie imię i nazwisko należy zastąpić odczytanymi z pliku tekstowego.

# plik = open('dane_osobowe.txt','r')
#
# imie = plik.readline().rstrip()
# nazwisko = plik.readline()
# print(f"Witaj {imie} {nazwisko}")
# plik.close()

# Zadanie 3
# Napisz program, który:
# a. zapisze w pliku losowe.txt 10 liczb losowych z zakresu od 1 do 100 w osobnych liniach.
# b. wyświetli sumę, minimum, maksimum, średnią liczb odczytanych z pliku losowe.txt
from random import randint

# plik = open('losowe.txt','r+')
# for i in range(10):
#     plik.write(str(randint(1,100))+"\n")
#
# numbers = []
# for i in plik:
#     i = i.strip()
#     numbers.append(int(i))
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# print(round(sum(numbers)/len(numbers),2))


# Zadanie 4
print("Zadanie 4")
file = open("ciagi.txt", "r")
for i in file:
    numbers = list(map(int, i.split()))
    if sum(numbers) % 2 == 0:
        print(*numbers)

# zadanie 5a
print("Zadanie 5a")
# file = open("slowa.txt", "r")
# number = 1
# for line in file:
#     print(number, line.strip())
#     number += 1
# file.close()

# Zadanie 5b
print("Zadanie 5b")
plik = open("slowa.txt","r")
slowa = list(plik.read().split())
print(len(slowa))
plik.close()

# Zadanie 5c
print("Zadanie 5c")
file = open("slowa.txt", "r")
for line in file:
    if line[0] == 'A':
        print(line.strip())
file.close()

# Zadanie 5d
print("Zadanie 5d")
file = open("slowa.txt", "r")
for line in file:
    if line.strip()[-1] == 'A':
        print(line.strip())
file.close()

# Zadanie 5e
print("Zadanie 5e")
file = open("slowa.txt", "r")
for line in file:
    print(line.strip(), len(line.strip()))
file.close()

# Zadanie 5f
print("Zadanie 5f")
file = open("slowa.txt", "r")
dlugosci = []
slowa = []

for line in file:
    dlugosci.append(len(line.strip()))
    slowa.append(line.strip())

mini = min(dlugosci)
maxi = max(dlugosci)

indexMin = dlugosci.index(mini)
indexMax = dlugosci.index(maxi)
print(slowa[indexMin], mini)
print(slowa[indexMax], maxi)

file.close()

# Zadanie  5g
print("Zadanie 5g")
file = open("slowa.txt", "r")
for line in file:
    if len(line.strip()) == 6:
        print(line.strip())
file.close()

# Zdadanie 5h
print("Zadanie 5h")
file = open("slowa.txt", "r")
for line in file:
    if line.count('O') > 0:
        print(line.strip(), line.count('O'))
file.close()

# Zadanie 5i
print("Zadanie 5i")
file = open("slowa.txt", "r")
ile = 0
for line in file:
    ile += line.count('A')
print(ile)
file.close()

zapis = open("wyniki.txt", "w")
# Zadanie 6a
print("Zadanie 6a")
zapis.write("Zadanie 6a\n")

file = open("liczby.txt", "r")
zapis.write(f"Długosc {len(file.readlines())}\n")
file.close()



# Zadanie 6b
print("Zadanie 6b")
zapis.write("Zadanie 6b\n")

file = open("liczby.txt", "r")
for line in file:
    if int(line.rstrip()[-1]) == 0:
        zapis.write(line)
file.close()

# Zadanie 6c
print("Zadanie 6c")
zapis.write("Zadanie 6c\n")

file = open("liczby.txt", "r")
for line in file:
    if int(line.strip()) == 0 or int(line.rstrip()[-3:]) == 000:
        zapis.write(line)
file.close()

# Zadanie 6d
print("Zadanie 6d")
zapis.write("Zadanie 6d\n")
file = open("liczby.txt", "r")
for line in file:
    if line.count('1') > line.count('0'):
        zapis.write(line)
file.close()

# Zadanie 6e
print("Zadanie 6d")
zapis.write("Zadanie 6d\n")
file = open("liczby.txt", "r")
for line in file:
    dec = int(line, 2)
    zapis.write(str(dec) + "\n")

file.close()
zapis.close()

# Zadanie 7
print("Zadanie 7")
zapis = open("losowe_w_linii.txt", "w")
for i in range(20):
    zapis.write(str(randint(1, 10)) + " ")
else:
    zapis.write("\n")

zapis.close()

file = open("losowe_w_linii.txt", "r")
numbers = list(map(int, file.readline().split()))
file.close()

liczby = [0] * 15
for line in numbers:
    liczby[int(line)] += 1

maksymalneLiczby = []

maks = max(liczby)
for i in range(len(liczby)):
    print(f"Liczba: {numbers[i]} ilosc: {liczby[i]}")
    if liczby[i] == maks:
        maksymalneLiczby.append(numbers[i])

print(set(maksymalneLiczby))