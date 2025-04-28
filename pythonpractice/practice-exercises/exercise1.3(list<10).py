# write a program that prints out all the elements of the list that are less than 5.

list = input("List the numbers you want to categorize (seperated by spaces): ")

numbers = [int(num) for num in list.split()]

less_than_five = [num for num in numbers if num < 5]

print(f"Numbers less than 5: {less_than_five}")


