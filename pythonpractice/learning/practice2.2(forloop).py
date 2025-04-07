# execute a block of code a fixed number of times
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects

for i in range(1, 11): # for (some counter) in some range (where do we begin and where do we end)
    print(i) # print the counter

for i in range(5): #prints numbers 0-4
    print(i)

for i in reversed(range(1, 6)): #prints numbers 1-5 (countdown using reversed function)
    print(i)
print("Happy New Year!") #prints Happy New Year! after the loop

for i in range(1, 11, 2): #prints odd numbers 1-10 (start at 1, end at 11, increment by 2)
    print(i)


credit_card = "1234 5678 9012 3456"

for i in credit_card: #prints each character in the string
    print(i)

    

    