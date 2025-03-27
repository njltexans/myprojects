# dictionaries are a collection of {key-value} pairs
# These pairs are ordered, changeable and do not allow duplicates
# Exmples could be: {item: name}, {item: price}

capitals = {"USA": "Washington D.C.", 
            "Canada": "Ottawa", 
            "Mexico": "Mexico City", 
            "India": "New Delhi"}
print(capitals)

# to see all attributes and methods of a dictionary use the dir() function
print(dir(capitals))
# to understand how they can be used use the help() function
print(help(capitals))


print(capitals.get("USA")) # get the value of the key "USA"
print(capitals.keys()) # get all the keys

# you can use get method to see if a value is in our dictionary
if capitals.get("USA"): # "USA" would be in dictionary, "China" would not
    print("That capital is in our dictionary")
else:
    print("That capital is not in our dictionary")

capitals.update({"Germany": "Berlin"}) # add a new key-value pair to the dictionary
capitals.update({"USA": "Las Vegas"}) # update the value of a key
capitals.pop("USA") # remove a key-value pair from the dictionary
capitals.clear() # remove all key-value pairs from the dictionary
capitals.popitem() # remove the last key-value pair from the dictionary

keys = capitals.keys() # get all the keys
values = capitals.values() # get all the values

for key in keys: # can use this to iterate through all the keys
    print(key)

items =  capitals.items() # get all the key-value pairs
for key, value in capitals.items(): # can use this to iterate through all the key-value pairs
    print(key, value)



