# Shopping cart program
# Practice for sets, tuples, etc.

lego_sets = []
prices = []
total = 0

while True:
    print("Welcome to the super cool Lego Store!")
    lego_set_name = input("Enter the name of the Lego set you would like to purchase (q to quit or view cart): ")
    if lego_set_name.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {lego_set_name} set:$ "))
        lego_sets.append(lego_set_name)
        prices.append(price)

print("---- YOUR SHOPPING CART ----:")
for lego in range(len(lego_sets)):
    print(f"{lego_sets[lego]}: ${prices[lego]}")
    total += prices[lego]

print(f"Total: ${total}")