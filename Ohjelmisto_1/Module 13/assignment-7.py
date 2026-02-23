import random

dice_count = int(input("Enter the number of dice: "))

total = 0

for _ in range(dice_count):
    roll = random.randint(1, 6)
    total += roll

print(total)
