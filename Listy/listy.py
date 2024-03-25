x = list(range(5))
# for item in x:
#   print(item)

# print()

# for item2 in range(5):
#   print(item2)

# print(list(range(5)))

# print(len(x))

# for i in range(len(x)):
#   print(x[i])

# for ele in x:
#   print(ele)

# deklaracja listy i iteracja po liście
# L = [3, 5, 8, 13, 17, 27]

# for item in L:
#   print(item, end=" ")

# print("\n")

# for i in range(len(L)):
#   print(L[i], end=" ")

#funkcje w listach
K = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(K)


# for i in range(K.count(7)):
#   K.remove(7)
# print(K)

# for i in range(K.count(7)):
#   K.pop(K.index(7))
# print(K)

maks = K[0]
for i in range(len(K)):
  if K[i] > maks:
    maks = K[i]
print(maks)

print(max(K))


# print("\n")

# K.append(3)
# print(K)

# print("\n")

# print(K.count(7))

# print("\n")

# print(K.index(7))

# print("\n")

# K.insert(2,4)
# print(K)

# print("\n")

# K.insert(len(K),4)
# print(K)

# print("\n")

# K.pop(0)
# print(K)

# print("\n")

# K.reverse()
# print(K)

# print("\n")

# K.sort(reverse=True)
# print(K)
