import math

def calculate_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * radius_m * radius_m
    return price_eur / area

d1 = float(input("Enter the diameter of the first pizza (cm): "))
p1 = float(input("Enter the price of the first pizza (eur): "))

d2 = float(input("Enter the diameter of the second pizza (cm): "))
p2 = float(input("Enter the price of the second pizza (eur): "))

unit1 = calculate_unit_price(d1, p1)
unit2 = calculate_unit_price(d2, p2)

if unit1 < unit2:
    print("The first pizza gives better value for money.")
elif unit2 < unit1:
    print("The second pizza gives better value for money.")
else:
    print("Both pizzas give the same value for money.")
