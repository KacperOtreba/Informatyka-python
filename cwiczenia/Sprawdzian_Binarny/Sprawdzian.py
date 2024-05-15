def decToBin(decymalna):
    binarna = ""
    while decymalna > 0:
        binarna = str(decymalna % 2) + binarna
        decymalna // 2
    return binarna

def lenik(napis):
    ile = 0
    for i in napis:
        ile += 1
    return ile


def binToDec(binarna):
    decymalna = 0
    for i in range(lenik(binarna)):
        if binarna[i] == "1":
            decymalna += 2 ** (lenik(binarna) - i - 1)
    return decymalna



with open("dane_systemy1.txt") as f:
    T = f.read().split()

print("Zadanie 1")

najwyzsza = T[1]
for i in range(0, lenik(T)):
    if i % 2 == 1:
        if binToDec(T[i]) > binToDec(najwyzsza):
            najwyzsza =  T[i]

najnizsza = T[1]
for i in range(0, lenik(T)):
    if i % 2 == 1:
        if binToDec(T[i]) < binToDec(najnizsza):
            najnizsza =  T[i]

print(binToDec(najwyzsza), "to najwyższa temperatura")
print(binToDec(najnizsza), "to najniższa temperatura")



print("Zadanie 2")
ileZłychPomiarów = 0
któryPomiar = 0
for i in range(0, lenik(T)):
    if i % 2 == 0:
        któryPomiar += 1
        liczba = binToDec(T[i])
        if 12 + (24*któryPomiar) != liczba:
            ileZłychPomiarów += 1

print(ileZłychPomiarów, "tyle razy pomiar był błędny")


print("Zadanie 3")

liczbaRekordów = 0
najwiekszaRóżnicaRekordów = 0
godzinaNajwiekszejRóżnicy = T[0]
najwiekszePodbicia = []


rekord = T[1]
poprzedniRekord = T[1]
for i in range(0, lenik(T)):
    if i % 2 == 1:
        if binToDec(T[i]) > binToDec(rekord):
            liczbaRekordów += 1
            poprzedniRekord = rekord
            rekord = T[i]

            dataRekordu = binToDec(T[i-1])
            if binToDec(rekord) - binToDec(poprzedniRekord) > najwiekszaRóżnicaRekordów:
                najwiekszaRóżnicaRekordów = binToDec(rekord) - binToDec(poprzedniRekord)
                godzinaNajwiekszejRóżnicy = binToDec(T[i-1])
                najwiekszePodbicia.clear()
                info = str(najwiekszaRóżnicaRekordów)+" "+  str(dataRekordu)
                najwiekszePodbicia.append(info)

            if binToDec(rekord) - binToDec(poprzedniRekord) == najwiekszaRóżnicaRekordów:
                info = str(najwiekszaRóżnicaRekordów)+" "+str(dataRekordu)
                najwiekszePodbicia.append(info)



print(liczbaRekordów, "to liczba dni rekordowych")
if (lenik(najwiekszePodbicia)==1):
    print(godzinaNajwiekszejRóżnicy, "to godzina kiedy było najwieksze podbicie dotychczasowego rekordu")    
else:
    for i in najwiekszePodbicia:
        print(i, " ")


print("Zadanie 4")
