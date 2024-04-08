# dec to bin
def decToBin(decymalna):
    binarna = " "
    while decymalna > 0:
        binarna = str(decymalna % 2) + binarna
        decymalna //= 2

    return binarna


# dec to bin reku - pojedyncze
def decToBinReku(decymalna):
    if decymalna == 0:
        return ""
    else:
        return decToBinReku(decymalna // 2) + str(decymalna % 2)


# dec to bin reku - laczny output
def decToBinReku2(decymalna):
    if decymalna == 0: return ""
    decToBinReku2(decymalna // 2)
    print(decymalna % 2, end="")


print(decToBin(37))
print(decToBinReku(37))
decToBinReku2(37)

print()


# bin to dec
def binToDec(binarna):
    suma = 0
    for i in range(0, len(binarna)):
        if binarna[i] == "1":
            suma += 2 ** (len(binarna) - i - 1)
    return suma


def binToDec2(binarna):
    suma = 0
    for i in range(len(binarna)):
        suma += 2 ** i * int(binarna[-i - 1])
    return suma


# Horner
def binToDecHorner(binarna):
    suma = 0
    for i in range(len(binarna)):
        suma = suma * 2 + int(binarna[i])
    return suma


print(binToDec("10011"))
print(binToDec2("10011"))
print(binToDecHorner("10011"))