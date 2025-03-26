#This is a practice project where I am creating a shopping cart that takes user input 

item = input("What item do you want to add to your cart? ")
quantity = int(input("How many do you want? "))
price = float(input("How much does it cost? "))
total = quantity * price

print(f"You have added {quantity} {item}s to your cart at ${price} each.")
print(f"Your total is ${round(total, 2)}")
