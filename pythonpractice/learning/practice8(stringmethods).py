# String methods practice 
# String methods are used to manipulate strings in Python.

name = input("Enter your name: ")

result = len(name) # returns the length of the string

print(result)


name.find("a") # returns the index of the first occurrence of the character in the string   
# finds first occurrence of the character in the string
# returns -1 if the character is not found
find = name.find("a") 
print(find)

name.rfind("a") # returns the index of the last occurrence of the character in the string
# finds last occurrence of the character in the string
# returns -1 if the character is not found

name.capitalize() # returns a copy of the string with the first character capitalized and the rest lowercased   

name.upper() # returns a copy of the string with all characters in uppercase

name.lower() # returns a copy of the string with all characters in lowercase

name.isdigit() # returns True if all characters in the string are digits, otherwise False
# only returns True if all characters are digits

name.isalpha() # returns True if all characters in the string are alphabetic, otherwise False
# only returns True if all characters are alphabetic

phone_number = "123-456-7890"
result = phone_number.count("-") # returns the number of occurrences of the character in the string
print(result)

phone_number.replace("-", " ") # returns a copy of the string with all occurrences of the old character replaced by the new character
# replaces all occurrences of the old character with the new character

print(help(str)) # returns a list of all string methods

