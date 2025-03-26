# indexing = accessing elements of a sequence using [] operator
#    string[index] - returns the character at the specified index   
#    string[start:stop] - returns the characters from start to stop-1
#    string[start:stop:step] - returns the characters from start to stop-1 with the specified step
#   string[:stop] - returns the characters from the beginning to stop-1     
#    string[start:] - returns the characters from start to the end
#    string[:] - returns the entire string

credit_number =  "1234-5678-9012-3456"

print(credit_number[0]) # returns the first character of the string

print(credit_number[0:4]) # returns the first four characters of the string
# You could also say credit_number[:4] to get the same result

print(credit_number[5:9]) # returns the characters from index 5 to 8

# if you need everything up to end of string no need to add end number to colon

print(credit_number[-1]) # returns the last character of the string

#can use nagative and positive indexing to get the same result

print(credit_number[::2]) # returns every other character of the string
#can change number of colons to skip different number of characters

