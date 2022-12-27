weight = float(input("Enter your weight: "))
unit = input("Kg (K) or Lbs (L): ")


if unit.upper() == "L":
    print("Your weight in kilograms is " + str((weight/0.45)))
elif unit.upper() == "K":
    print("Your weight in pounds is " + str((weight * 2.2)))
else:
    print("Invalid input")