# File detection 

import os #import sys which allows python to interact with the operating system

file_path = "stuff/test.txt" #specify the file path, in this case it is a text file that is in a folder called stuff
# You can also paste in the exact path to the file such as "C:/Users/YourName/Desktop/test.txt"

# Check if the file exists
if os.path.isfile(file_path): #os.path.isfile checks if the file exists
    print(f"{file_path} exists.") #print if the file exists

    if os.path.isfile(file_path): #os.path.isfile checks if the file exists
        print("That is a file.") #print if the file exists
        
    elif os.path.isdir(file_path): #os.path.isdir checks if the file is a directory
        print("That is a directory.")


else:
    print(f"{file_path} does not exist.")


