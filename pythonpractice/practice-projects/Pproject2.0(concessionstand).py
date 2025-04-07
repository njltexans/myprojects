# Concession stand project

# Using dictionary {key: value} to store the items and their prices

movie_concessions = { "popcorn": 5.00, 
                     "soda": 3.00, 
                     "candy": 4.00, 
                     "hotdog": 7.00, 
                     "nachos": 6.00,
                      "pizza": 8.00,
                      "fries": 5.00,
                      "ice cream": 4.00,}

cart = []
total = 0

print("Welcome to Noah's concessions! The best snackaros in the world! ")
print("MENU".center(20, "-"))
for item, price in movie_concessions.items():
    print(f"{item.capitalize():10}: ${price:.2f}")
print("-" * 20)

while True:  # Loop to keep asking for items until the user quits
    item = input("What would you like to order? (q to quit) ").lower()
    if item == "q":
        break
    elif movie_concessions.get(item) is not None:
        cart.append(item)
        total += movie_concessions[item]
    else:
        print("We don't have that item. Pick something we have.")



print("--YOUR SNACKARO ORDER--")
for item in cart:
    total += movie_concessions[item]
    print(f"{item.capitalize():10}: ${movie_concessions[item]:.2f}")

print("TOTAL".center(20, "-"))
print(f"${total:.2f}".center(25))
print("Thank you for shopping at Noah's concessions! Enjoy the movie!")



