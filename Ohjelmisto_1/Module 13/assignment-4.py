import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess < secret_number:
        print("Liian pieni arvaus")
    elif guess > secret_number:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break
