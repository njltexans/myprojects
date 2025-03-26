#  nested loops = loops written within another loop (outer and inner loop)
#                  outer loop
#                      inner loop


for i in range(3): #outer loop, prints the numbers 1-10 3 times
    for x in range(1, 11): #inner loop
        print(x, end="") # prints numbers 1-10 without new line
    print() #prints a new line after each iteration



#Example project (printing a rectangle with user input)

rows = int(input("Enter the number of rows: ")) #user input for rows
columns = int(input("Enter the number of columns: ")) #user input for columns
symbol = input("Enter a symbol to use: ") #user input for symbol

for i in range(rows): #outer loop
    for x in range(columns): #inner loop
        print(symbol, end="") #prints the symbol without a new line
    print() #prints a new line after each iteration
