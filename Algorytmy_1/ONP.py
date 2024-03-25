T = [12, 7, 5, "-", "/", 4, 2, 5, "*", "+", "-"]
A = ["-", "/", "*", "+"]
B = []
for i in T:
    if i not in A:
        B.append(i)
print(B)
