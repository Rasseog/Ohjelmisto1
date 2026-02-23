airports = {}

while True:
    choice = input(
        "Choose an action:\n"
        "1 = Enter a new airport\n"
        "2 = Fetch airport information\n"
        "3 = Quit\n"
        "Enter your choice: "
    )

    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name

    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print(airports[icao])
        else:
            print("Airport not found")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
