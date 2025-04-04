# Writing python files (.txt, .csv, .json)

#.txt files

txt_data = "I love me some pizza "

file_path = "stuff/test.txt" #specify the file path, in this case it is a text file that is in a folder called stuff

with open(file=file_path, mode="w") as file: #open the file in write mode, with statement is used to open the file and automatically close it after the block of code is executed
    # "w" mode will overwrite the file if it already exists
    # "a" mode will append the data to the file if it already exists
    # "r" mode will read the file
    file.write(txt_data) #write the data to the file
    print(f"Data written to {file_path}") #print if the data is written to the file
    # file.close() #close the file, not needed because with statement automatically closes the file



#Json

import json #import json module to work with json files
import os #import os module to work with file paths
import random #import random module to generate random numbers

employee = {
    "name": "John Doe",
    "age": 30,
    "department": "IT",
    "salary": 50000, }

file_path = "stuff/employee.json" #specify the file path, in this case it is a json file that is in a folder called stuff
# You can also paste in the exact path to the file such as "C:/Users/YourName/Desktop/employee.json"

try:
    with open(file=file_path, mode="w") as file: #open the file in write mode, with statement is used to open the file and automatically close it after the block of code is executed
        json.dump(employee, file) #dump the data to the file
        print(f"Data written to {file_path}")
except FileNotFoundError:
    print(f"{file_path} does not exist.") #print if the file does not exist
except json.JSONDecodeError:
    print(f"Error decoding JSON data in {file_path}") #print if there is an error decoding the json data
except Exception as e:
    print(f"An error occurred: {e}") #print if there is any other error
finally:
    print("File closed") # file.close() is not needed because the with statement automatically closes the file
        # file.close() #close the file, not needed because with statement automatically closes the file


# .csv files

import csv #import csv module to work with csv files
import os #import os module to work with file paths
import random #import random module to generate random numbers

employee = [["name", "age", "job"], ["Joe", 35, "Police Officer"]
["Anna", 28, "Teacher"], ["Mike", 40, "Engineer"]]

file_path = "stuff/employees.csv"  # specify the file path, in this case it is a csv file that is in a folder called stuff

try:
    with open(file=file_path, mode="w", newline="") as file:  # open the file in write mode
        writer = csv.writer(file)  # create a csv writer object
        writer.writerows(employee)  # write the rows to the csv file
        print(f"Data written to {file_path}")
except FileNotFoundError:
    print(f"{file_path} does not exist.")  # print if the file does not exist
except Exception as e:
    print(f"An error occurred: {e}")  # print if there is any other error
finally:
    print("File closed")  # file.close() is not needed because the with statement automatically closes the file