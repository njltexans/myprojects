# collection = single "variable" that holds multiple values
# list = [] collection which is ordered and changeable. Allows duplicate members.
# tuple = () collection which is ordered and unchangeable. Allows duplicate members.
# set = {} collection which is unordered and unindexed. No duplicate members.

#collection

fruits = ["apple", "orange", "banana", "grapes"]
print(fruits)

# can use index to access elements in a list [0 for apple, 1 for orange, 2 for banana, 3 for grapes]
# can also list specfic elements in a list using slicing fruits[1:3] = ["orange", "banana"]
# can also change elements in a list fruits[1] = "kiwi" = ["apple", "kiwi", "banana", "grapes"]

for i in fruits: #can interate through a list
    print(i)

#dir function can be used to see all the methods that can be used with a list
#help function can be used to see how to use a method
#len function can be used to see how many elements are in a list
# in function can be used to check if an element is in a list (is a boolean)
# append method can be used to add an element to a list
# insert method can be used to add an element at a specific index
# remove method can be used to remove an element from a list
#sort method can be used to sort a list in ascending order or alphabetical order
# reverse method can be used to reverse a list
# pop method can be used to remove the last element from a list
# clear method can be used to remove all elements from a list

#Set
fruits = {"apple", "orange", "banana", "grapes"}
print(fruits)

# we can add or remove elements from a set but can not change elements
#can not use index to access elements in a set since they are unordered

#Tuple
fruits = ("apple", "orange", "banana", "grapes")
print(fruits)

