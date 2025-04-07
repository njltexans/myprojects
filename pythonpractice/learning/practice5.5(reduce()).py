# reduce(function, collection) reduces the elements in a collection to a single value
# by applying the function cumulatively to the items of the collection.
# The function must take two arguments and return a single value.

from functools import reduce # importing reduce from functools module

prices = [10.99, 20.99, 5.99, 15.99] # list of prices

total = reduce(lambda x, y: x + y, prices) # using reduce to sum the prices
print(f"The total price is: ${total:.2f}") # printing the total price
