numbers = []

while True:
    user_input = input("Enter a number: ")

    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)

numbers.sort(reverse=True)

print("The greatest numbers in descending order:")
for i in range(min(5, len(numbers))):
    print(numbers[i])