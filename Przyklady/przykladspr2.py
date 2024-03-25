######################################3
a = int(input("Licz1: "))
b = int(input("Mian1: "))
A = a

c = int(input("Licz2: "))
d = int(input("Mian2: "))
C = c

e = int(input("Licz3: "))
f = int(input("Mian3: "))
E = e

B = b
D = d
temp = b * d
while D > 0:
    B, D = D, B % D
nwwbd = temp // B


X = nwwbd
F = f
temp = nwwbd * f
while F > 0:
    X, F = F, X % F
nww = temp // X

A *= (nww // b)
C *= (nww // d)
E *= (nww // f)

print(f"{A}/{nww}")
print(f"{C}/{nww}")
print(f"{E}/{nww}")
print(f"suma tych ułamków to {A + C + E} / {nww}")

#######################################

# for a in range(1,5000):
#     for b in range(1,5000):
#         sumadziel1 = 0
#         for i in range(1,a):
#             if a % i == 0:
#                 sumadziel1 += i
#         sumadziel2 = 0
#         for j in range(1,b):
#             if b % j == 0:
#                 sumadziel2 += j
#         if sumadziel1 == b and sumadziel2 == a:
#             print(a, b)



# sumadziel1 = 0
# for i in range(1,n):
#     if n % i == 0:
#         sumadziel1 += i
