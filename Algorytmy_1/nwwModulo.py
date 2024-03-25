a, b = int(input()), int(input())
temp = a * b
while b > 0:
  a, b = b, a % b
print(f"NWW = {temp // a}")