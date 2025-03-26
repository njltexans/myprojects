# Practice project of creating a countdown timer using python using different kinds of loops

import time

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1): # This will make the program to countdown from the input using a step of -1
    seconds = i % 60
    minutes = i // 60 % 60 # This will make sure it does not display more than 60 minutes
    hours = i // 3600 % 24 # This will make sure it does not display more than 24 hours
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) # This will make the program to sleep for 1 second (delay display in ternminal)

print("TIMES UP!!!")

