def gallons_to_liters(gallons):
    return gallons * 3.785


while True:
    gallons = float(input("Enter gallons: "))

    if gallons < 0:
        break

    liters = gallons_to_liters(gallons)
    print(f"{liters} liters")
