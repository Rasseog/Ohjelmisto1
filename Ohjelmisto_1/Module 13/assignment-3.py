numbers = []

while True:
    user_input = input("Enter a number (empty to stop): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

if numbers:
    print(f"Smallest: {min(numbers)}")
    print(f"Largest: {max(numbers)}")
