plik = open("ciag.txt", "r")
ciag = list(map(int, plik.readline().rstrip().split()))
plik.close()

maks = 0

for i in range(1, len(ciag) + 1):
    for j in range(0, len(ciag) - i + 1):
        print(*ciag[j:i + j])
        suma = sum(ciag[j:i + j])
        if suma > maks:
            maks = suma

print(maks)