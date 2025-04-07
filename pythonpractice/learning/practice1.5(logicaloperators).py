# Logical operators in python (used in conditional statements)
# and, or, not
# and = both conditions must be true
# or = one of the conditions must be true
# not = reverse the result, if the result is true then it will return false


temp = 25
sunny = True

if temp > 0 and temp < 30:
    print("The temperature is good for a sunday stroll")
else:
    print("The temperature is not good for a sunday stroll")


if temp <= 0 or temp >= 30:
    print("The temperature is good for a sunday stroll")
else:
    print("The temperature is not good for a sunday stroll")    


if sunny :
    print("The weather is sunny")
else:
    print("The weather is not sunny")

if not sunny:
    print("The weather is not sunny")
else:
    print("The weather is sunny")