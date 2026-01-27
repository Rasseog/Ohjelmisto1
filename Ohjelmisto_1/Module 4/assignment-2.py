while True:
    inches = float(input("Enter length in inches (negative value to quit): "))

    if inches < 0:
        print("Program ended.")
        break

    cm = inches * 2.54
    print(f"{inches} inches is {cm:.2f} centimeters")