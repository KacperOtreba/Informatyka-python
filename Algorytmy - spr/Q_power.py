def potega(a,n):
    w = 1
    while n > 0:
        if n % 2 == 1:
            w *= a
        a *= a
        n //= 2
    return w

print(potega(2,4))