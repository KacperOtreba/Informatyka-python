def f(x):
    return -1*(x**3) + 2*(x**2) + x

def g(x):
    return -1*(x**3) + 2*(x**2) + x + 1

def calka(a,b, n, fun):
    dx = (b-a)/n
    suma = 0
    for i in range(n):
        suma+= fun(a + i*dx + dx/2) * dx
    return suma

# n = 17
# 1kg nawozu = 5m2
# 1 worek nawozu = 5kg
# 1 worek nawozu = 25m2 czyli 0,025km2
# 1km = 1000m czyli 1m = 0,001km czyli 25m = 0,025km


Pole_dolnej_dzialki = calka(0,2, 17, f)
Pole_calej_dzialki = 4*2
Pole_dzialki_podRzeka = calka(0,2,17, g)

Pole_gornej_dzialki = Pole_calej_dzialki - Pole_dzialki_podRzeka

Pole_dzialki_bezRzeka = Pole_dolnej_dzialki + Pole_gornej_dzialki

Ilosc_workow = Pole_dzialki_bezRzeka / 0.025

print("Powierzchnia dolnej czesci dzialki to ",Pole_dolnej_dzialki, "km^2")
print("Powierzchnia górnej działki to ",Pole_gornej_dzialki, "km^2")
print("Powierzchnia działki pod rzeką",Pole_dolnej_dzialki,"km^2")
print("Potrzeba", Ilosc_workow, "worków nawozu by to nawieźć nawozem do traw firmy: Nawóz do traw")