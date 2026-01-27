import random

def roll_dice(sides):
    return random.randint(1, sides)

max_number = int(input("Enter the maximum number on the dice: "))

while True:
    result = roll_dice(max_number)
    print(result)

    if result == max_number:
        break