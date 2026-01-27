import random

N = int(input("Number of random points: "))

n = 0
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        n += 1

    i += 1

pi_approximation = 4 * n / N

print(f"Approximation of pi: {pi_approximation}")