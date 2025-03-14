# 10. Podciągi - sumowanie
# Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4

plik = open("ciag.txt", "r")
ciag = list(map(int, plik.readline().rstrip().split()))
plik.close()
nSuma = 0

for i in range(len(ciag)-2):
    suma = sum(ciag[i:i+3])
    if suma > nSuma:
        nSuma = suma
print(nSuma)
