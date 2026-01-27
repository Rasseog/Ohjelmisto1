import math

def calculate_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100  # cm → m
    area_m2 = math.pi * radius_m ** 2
    return price_euros / area_m2

d1 = float(input("Enter the diameter of the first pizza (cm): "))
p1 = float(input("Enter the price of the first pizza (euros): "))

d2 = float(input("Enter the diameter of the second pizza (cm): "))
p2 = float(input("Enter the price of the second pizza (euros): "))

unit_price1 = calculate_unit_price(d1, p1)
unit_price2 = calculate_unit_price(d2, p2)

print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")
