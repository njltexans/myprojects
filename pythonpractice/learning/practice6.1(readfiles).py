# Reading files using python (.txt, .csv, .json)

file_path = "C:/Users/andre/OneDrive/Documents/GitHub/python-learning/learning/practice51%28readfiles%29.txt" # path to the file
file = open(file_path, "r") # open the file in read mode

with open(file_path, "r") as file: # open the file in read mode
    lines = file.readlines() # read all lines in the file
    for line in lines:
        print(line.strip()) # print each line without leading/trailing whitespace

try:
    with open(file_path, "r") as file: # open the file in read mode
        lines = file.readlines() # read all lines in the file
        for line in lines:
            print(line.strip()) # print each line without leading/trailing whitespace
except FileNotFoundError:
    print(f"File not found: {file_path}")
finally:
    file.close()
    # file.close() # close the file
    # print("File closed")
# file.close() # close the file

