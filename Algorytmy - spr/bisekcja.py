# Metoda bisekcji
def f(x):   # Definiowanie funkcji 
   return x ** 2 - 8 * x + 12


# Metoda bisekcji - poszukiwanie miejsca zerowego funkcji, czyli takiego x, dla ktorego f(x) = 0
# 2 warianty
def bisekcja(a, b, epsilon):    # epsilon - o ile precyzyjny ma byc wynik
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
print(bisekcja(-5, 50, 0.1))

def bisekcja_2(a, b, n):    # n - ilosc krokow
    for i in range(n):
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

print(bisekcja_2(-5, 50, 10))
