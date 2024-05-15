# p - liczba, z ktorej szukamy pierwiastek
# n - ilosc krokow
def newton_raphson1(p, epsilon):
    a = p
    b = 1
    while a - b > epsilon:
        a = (a + b) / 2
        b = p / a
    return a

print(newton_raphson1(4900, 0.000001))



def newton_raphson2(p, n):
    a = p
    b = 1
    for i in range(n):
        a = (a + b) / 2
        b = p / a
    return a

print(newton_raphson2(4900, 7))
