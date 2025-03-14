plik = open("ciag.txt", "r")
ciag = list(map(int, plik.readline().rstrip().split()))
plik.close()

nSuma = 0
for i in range(len(ciag)-2):
    suma = sum(ciag[i:i+3])
    if suma > nSuma:
        nSuma = suma
        npodciag = ciag[i:i+3]

print(npodciag)