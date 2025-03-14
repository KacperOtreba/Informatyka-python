# 07. Sortowanie przez scalanie
# Link do dysku: https://drive.google.com/drive/folders/1PO3HAZ2CR4QG80sSmwte5FJ7bo5M8KE4


def scal(T,l,srodek,p):
    i = l
    j = srodek + 1
    k = l
    while i <= srodek and j <= srodek:
        if T[i] < T[j]:
            pom[k] = T[i]
            i += 1
        else:
            pom[k] = T[j]
            j += 1
        k += 1
    while i <= srodek:
        pom[k] = T[i]
        i += 1
        k += 1
    while j <= srodek:
        pom[k] = T[j]
        j += 1
        k += 1
    for i in range(l,p):
        T[i] = pom[i]



def sortuj(T,l,p):
    if l < p:
        srodek = (l+p)//2
        sortuj(T,l, srodek)
        sortuj(T,srodek+1,p)
        scal(T,l,srodek, p)


# Zadanie 1
# Napisz program, który wczyta z klawiatury ciąg liczb rozdzielonych spacjami, a następnie posortuje
# ten ciąg za pomocą algorytmu przedstawionego w przykładzie i wyświetli po posortowaniu.

ciag = input("Podaj ciąg do posortowania: ")
ciag = list(map(int,ciag.split()))
pom = [0] * (len(ciag))
n = len(ciag)
sortuj(ciag,0, n-1)
print(ciag)