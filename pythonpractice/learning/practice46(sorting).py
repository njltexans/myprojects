# Sorting .sort() method or sorted() function
# Lists[], Tuples(), Dictionaries{}, Objects
# .sort() method sorts the list in place and returns None
# sorted() function returns a new sorted list from the elements of any iterable

#Lists

fruits = ['banana', 'apple', 'cherry', 'coconut']

fruits.sort() # sort the list in alphabetical order
print(fruits) # ['apple', 'banana', 'cherry', 'coconut']
# fruits.sort(reverse=True) # sort the list in reverse alphabetical order

#Tuples

fruits = ('banana', 'apple', 'cherry', 'coconut')

fruits = sorted(fruits) # sort the tuple in alphabetical order
print(fruits) # ['apple', 'banana', 'cherry', 'coconut']
# fruits = sorted(fruits, reverse=True) # sort the tuple in reverse alphabetical order


#Dictionaries

fruits = {'banana': 105, 'apple': 200, 'cherry': 31, 'coconut': 400}
fruits = dict(sorted(fruits.items())) # sort the dictionary by keys
print(fruits) # {'apple': 200, 'banana': 105, 'cherry': 31, 'coconut': 400}
# fruits = dict(sorted(fruits.items(), reverse=True)) # sort the dictionary by keys in reverse order
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1])) # sort the dictionary by values
# print(fruits) # {'cherry': 31, 'banana': 105, 'apple': 200, 'coconut': 400}
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True)) # sort the dictionary by values in reverse order


#Objects
class fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self): # string representation of the object
        return f"{self.name}: {self.calories} calories"
    
fruits = [fruit('banana', 105), fruit('apple', 200), fruit('cherry', 31), fruit('coconut', 400)]
fruits = sorted(fruits, key=lambda x: x.calories) # sort the list of objects by calories
print(fruits) # [cherry: 31 calories, banana: 105 calories, apple: 200 calories, coconut: 400 calories]
# fruits = sorted(fruits, key=lambda x: x.calories, reverse=True) # sort the list of objects by calories in reverse order
# print(fruits) # [coconut: 400 calories, apple: 200 calories, banana: 105 calories, cherry: 31 calories]