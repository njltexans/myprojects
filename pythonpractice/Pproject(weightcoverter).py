#Python Weight Converter Program (convert pounds to kilograms or kilograms to pounds)

weight = float(input("Enter your weight: "))
if weight > 200:
    print("Gotta lay off those cookies tubbo")

unit = input("L(bs) or K(g): ")

if unit == "L" or unit == "l":
    converted = weight * 0.45
    print(f"You are {round(converted), 1} kilos")
elif unit == "K" or unit == "k":
    converted = weight / 0.45
    print(f"You are {round(converted, 1)} pounds")
else:
    print("Invalid unit")