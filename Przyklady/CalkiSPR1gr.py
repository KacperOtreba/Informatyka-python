def f(x):
    return ((x**4)/500) - ((x**2)/200) - (3/250)

def g(x):
    return (-((x**3)/30)) + (x/20) + (1/6)

def calka(a,b, n, fun):
    dx = (b-a)/n
    suma = 0
    for i in range(n):
        suma+= fun(a + i*dx + dx/2) * dx
    return suma



bokAD = (19+61/125) + (32+2/3)
bokAB = 8
prosABCD = bokAD * bokAB
print(prosABCD)


dodatniProstokat = (19+61/125) * 8
dodatniaKurtyna = dodatniProstokat - calka(2,10,100,f)


ujemnyProstakat = (32+2/3) * 8
ujemnaKurtyna = ujemnyProstakat - abs(calka(2,10,100, g))


calaKurtyna = dodatniaKurtyna + abs(ujemnaKurtyna)
pozostalePole = prosABCD - calaKurtyna


print("Pole pozostałe po wykrojeniu: ",pozostalePole)
