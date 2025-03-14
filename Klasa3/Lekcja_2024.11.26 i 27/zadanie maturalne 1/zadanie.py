plik = open("pi_przyklad.txt","r")
ciag = list(map(int, plik.read().split()))
plik.close()

czy_rosnie = True
n = len(ciag)
fragment = [ciag[0]]
for i in range(1,n):
    if czy_rosnie and ciag[i]>fragment[-1]:
        fragment.append(ciag[i])
    else:
        czy_rosnie = False
        fragment.append(ciag[i])
    if not czy_rosnie and ciag[i]<fragment[-1]:
        fragment.append(ciag[i])