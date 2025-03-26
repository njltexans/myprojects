#Creating python compound interest calculator

principle = 0
irate = 0
time = 0

#gather the user inputs

while principle <= 0:
    principle = float(input("Enter the principle amount:$ "))
    if principle <= 0:
        print("Principle amount must be greater than $0")

while irate <= 0:
    irate = float(input("Enter the interest rate (%): "))  # Prompt includes "%"
    if irate <= 0:
        print("Interest rate must be greater than 0%")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than 0") 

#calculate the compound interest
compound_interest = principle * (1 + irate / 100) ** time

print(f"Your compound interest after {time:.0f} years at a {irate:.2f}% interest rate is: ${compound_interest:.2f}")