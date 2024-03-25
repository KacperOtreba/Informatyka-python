def NR_EPS(x, eps):
    a = x
    b = 1
    while abs(a - b) > eps:
        a = (a + b) / 2
        b = x / a
    return a


def NR(x, n):
    a = x
    b = 1
    for i in range(n):
        a = (a + b) / 2
        b = x / a
    return a


print(NR_EPS(49, 0.001))
print(NR(49, 7))
