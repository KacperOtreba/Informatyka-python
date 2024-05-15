# zad 1
# n = input()
# for i in range(len(n)):
#     print(" " * (len(n)-i-1), n[:i+1])


# zad 2
# n = input()
# ilosc = 0
# for i in range(1,len(n)):
#     if n[i-1] == n[i]:
#         ilosc += 1
# print(ilosc)


# zad 3
# n = input()
# dup = []
# ilosc = 0
# for i in range(len(n)):
#     if n[i] not in dup:
#         dup.append(n[i])
#         ilosc += 1
# print(dup)
# print(ilosc)


# zad 4
# n = input()
# nowe = ""
# for i in range(len(n)//2):
#     nowe += n[i]
#     nowe += n[len(n) - i -1]

# if len(n) % 2 != 0:
#     nowe += n[len(n)//2]

# print(nowe)