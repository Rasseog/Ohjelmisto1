import random

N = int(input("Enter the number of random points: "))

inside = 0
count = 0

while count < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        inside += 1

    count += 1

pi_approx = 4 * inside / N
print(pi_approx)
