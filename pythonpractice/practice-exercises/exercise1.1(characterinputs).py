import time

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = 2025
oldageyear = year + (100 - age)

print(f"Nice to meet you {name}!")

time.sleep(1)
if age < 21:
    print("Wow you are a youngin")
elif 21 < age < 35:
    print("You're still pretty young and hip")
else:
    print("You are ollllddddd")

time.sleep(2)
superold = input("By the way, you want to know the year you'll turn 100? (Y or N to be lame)").lower()

if superold == "y":
    print(f"You will turn 100 years old in the year {oldageyear}")

elif superold == "n":
    print("You're no fun. LAAAMMMEEEE!")

else:
    print("Not a valid entry, LAME")