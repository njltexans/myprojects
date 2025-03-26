#input function allows acceptance of user input into console

name = input("Enter your name: ") #storing user input in variable to be used later

print(f"Hello, {name}") #printing user input with a greeting

age = int(input("How old are you: ")) #storing user input in variable to be used later

if age <= 18:
    print("You are a youngin")
elif 18 < age < 31:
    print("You are livin life!")
else:
    print("You are an unc")
    