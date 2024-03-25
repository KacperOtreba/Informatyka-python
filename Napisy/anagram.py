# ANAGRAM PRZEZ SORTOWANIE
a, b = input(), input()
X, Y = list(a), list(b)
X.sort()
Y.sort()
a = "".join(X)
b = "".join(Y)
print(a,b)
if a == b:
    print("TAK")
else:
    print("NIE")


# ANAGRAM PRZEZ TABLICE

# a, b = input(), input()
# X, Y = [0] * 150, [0] * 150
# for i in range(len(a)):
#     X[ord(a[i])] += 1
# print(X)
