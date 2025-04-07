# 2d lists 

fruits =     ["apple", "orange", "banana", "grapes"]

vegetables = ["carrot", "lettuce", "cucumber", "onion"]

meats =      ["beef", "chicken", "pork", "lamb"]

grocerires = [fruits, vegetables, meats]


print(grocerires) #prints entire 2d list

print(grocerires[0]) #prints fruits list, can change index to print other lists

print(grocerires[0][1]) #prints orange, can change index to print other elements in the list
# you need two indexes to access an element in a 2d list, one element returns the entire list


shopping_day = [["sweater", "socks", "scarf"],   #This would also be a 2d list with 3 lists inside
                ["shorts", "tshirt", "sandals"],
                ["jacket", "sweatshirt", "joggers"]]

print(shopping_day) #prints entire 2d list

print(shopping_day[0]) #prints first list, can change index to print other lists

print(shopping_day[0][1]) #prints socks, can change index to print other elements in the list

for collection in shopping_day: 
    for item in collection: 
        print(item, end = " ") #prints all elements in the 2d list
    print() #prints a new line after each list


# creating a keypad using a 2d list

row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
row4 = ["*", "0", "#"]

keypad = [row1, row2, row3, row4]

for row in keypad:
    for key in row:
        print(key, end = " ")
    print() #prints a new line after each row