# practice typecasting (converting data types, i.e integer to string, string to integer, float to integer, boolean to float, etc)
# Explicit vs. Implicit typecasting

name = "Joegoonsmith" # string
age = 25 # integer
net_worth = 1.25 # float
rich_in_money = False # boolean
favorite_number = 15 # integer

# Explicit typecasting
print(type(name))
print(type(age))
print(type(net_worth))
print(type(rich_in_money))

#changing value to a float
age = float(age)
print(age)

#changing value into a integer
net_worth = int(net_worth)
print(net_worth)

#changing value into a string
rich_in_money = str(rich_in_money)
print(rich_in_money)

#changing value into a boolean
favorite_number = bool(favorite_number)
print(favorite_number) #any number but zero will return as True in boolean

# Implicit typecasting, when value or variable is automatically converted to another data type
# Example:

x = 5
y = 2.5

x = x/y
print(x) # 2.0, integer, automatically converted to float because of the float value of y