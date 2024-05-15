import random


def MonteCarlo(n):
    c = 0
    for i in range(n):
        x = random.uniform(-1,1)    # The uniform() method returns a random floating number between the two specified numbers (both included).
        y = random.uniform(-1,1)
        if x ** 2 + y ** 2 <= 1:
            c += 1
    return 4 * c / n

print(MonteCarlo(999999))
