numbers = []

while True:
    user_input = input("Enter a number (empty to stop): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

top_five = numbers[:5]

for number in top_five:
    print(number)
