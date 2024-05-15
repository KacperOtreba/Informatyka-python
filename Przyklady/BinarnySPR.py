# 11011 * 101

# sposób 1
a = input()
b = input()

M = []

for i in range(len(b)):
    if b[len(b)-1-i] == "0":
        M.append("00000")
    else:
        M.append(a)

print(M)

M[0] = "00"+M[0]
M[1] = "0"+M[0]+"0"
M[2] = M[0]+"00"

print(M)

W = "0000000"

for i in range(len(W)):
    W = W[:i] + str(int(W[i]) + int(M[0][i]) + int(M[2][i]) + int(M[2][i])) + W[i+1:]

print(W)
W = "0" + W
for i in range(1,len(W)):
    W = W[:-i] + str(int(W[-i] % 2)) + W[-i+1:]
    W = W[:-i-1] + str(int(W[-i] // 2)) + int(W[-i-1]) + W[-i:]
print(W)