# validate user input expercise 
# 1. Username is no more than 15 characters
# 2. Username contains only alphabetic characters
# 3. Username is not empty

username = input("Enter your username: ")

if len(username) <= 15 and username.isalpha() and username != "":
    print("Valid username")
else:
    print("Invalid username")
# Output: Enter
