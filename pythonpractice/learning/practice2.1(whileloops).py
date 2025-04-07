# While loops = a loop that keeps running as long as the condition is True

#Example 1

name = input("Enter your name: ")

while name == "": # while this condition is True, keep running the loop (until it's not) or in this case, when a user enters a name
    print("You didn't write anything man :(")
    name = input("Enter your name: ") # need this prompt so that the loop can end

print(f"Hey {name}! ")

# Example 2

age = int(input("Enter your age: "))

while age < 0
    print("You can't be negative years old")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")


# Example 3

cologne = input ("Enter your favorite cologne (q to quit): ")

while cologne != "q":
    print(f"Your favorite cologne is {cologne}")
    cologne = input ("Enter your favorite cologne (q to quit): ")
print("Goodbye!") # this will print when the loop is done


