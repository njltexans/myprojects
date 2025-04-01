# Simple encrytion practice program in python

import random
import string


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+ "

chars = list(chars)

key = chars.copy()
random.shuffle(key)

#Encryption

message = input("Enter a message to encrypt: ")
encrypted_message = ""

for letter in message:
    if letter in chars: #if the letter is in the chars list
        index = chars.index(letter) #get the index of the letter
        encrypted_message += key[index] #add the letter at the same index in the key list
    else:
        encrypted_message += letter #if the letter is not in the chars list, add the letter as is

print(f"orginal message: {message}")
print(f"encrypted message: {encrypted_message}")

#Decryption

encrypted_message = input("Enter a message to decrypt: ")
message = ""

for letter in encrypted_message:
    if letter in key: 
        index = key.index(letter) 
        message += chars[index]  # Use chars[index] for decryption
    else:
        message += letter  # Append to message, not encrypted_message

print(f"encrypted message: {encrypted_message}")
print(f"original message: {message}")
