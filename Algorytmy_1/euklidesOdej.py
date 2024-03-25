a, b = int(input("Podaj pierwszą liczbe: ")), int(input("Podaj drugą liczbe: "))
while a != b :
  if   a > b : a -= b
  if   b > a : b -= a
print("NWD tych liczb to:", a)


# a * b = NWD(a,b) * NWW(a,b) <-- wzór
# NWW(a,b) = a * b / NWD(a,b)



# a = int(input())
# b = int(input())
# while a!= b:
#   if a > b : a -= b
#   if b > a : b -= a
# print(a)
