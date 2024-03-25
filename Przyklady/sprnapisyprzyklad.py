# zad 1
# n = input()
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i] == n[j]:
#             print(n[i+1:j])

# zad 2
# n = input()
# print(n[::-1])
# print("".join(list(reversed(n))))

# zad 3
n = input()
flaga = True
for i in range(len(n)-1):
    if ord(n[i]) <= ord(n[i+1]):
        pass
    else:
        flaga = False
        break

if flaga:
    print("tak")
else:
    print("nie")

# zad 1
# a = input()
# b = input()
# if a in b:
#     print("jest")
# else:
#     print("nie jest")

# zad 2
# n = list(input())
# slowo = ["b","a","z","a"]
# flaga = True
# for item in slowo:
#     if item in n:
#         n.remove(item)
#     else:
#         flaga = False
#         break

# if flaga:
#     print("tak")
# else:
#     print("nie")

# zad 3
# n = list(input())
# baza = n
# list(baza)
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i] == n[j]:            
#             n.remove(n[i])
# print(n)

# for i in range(len(baza)):
#     for j in range(i+1,len(baza)):
#         if baza[i] == baza[j]:            
#             baza.remove(baza[j])
# print(baza)


# n = input()
# for i in range(len(n)):
#     print(n[:i+1])


# zad 2
# n = input()
# ilosc = 0
# for i in range(1,len(n)):
#     if n[i-1] == n[i]:
#         ilosc += 1
# print(ilosc)


# zad 1
# n = input()
# dup = []
# ilosc = 0
# for i in range(len(n)):
#     if n[i] not in dup:
#         dup.append(n[i])
#         ilosc += 1
# print(ilosc)

# print(len(set(n)))


# zad 2
# n = input()
# nowe = ""
# for i in range(len(n)//2):
#     nowe += n[i]
#     nowe += n[len(n) - i - 1]

# if len(n) % 2 != 0:
#     nowe += n[len(n)//2]
# print(nowe)