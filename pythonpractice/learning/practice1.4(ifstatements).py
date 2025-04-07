# if statements 
# used to do some code if a condition is true
# if not true, the code is skipped or Else to do something else
# elif is used to check multiple conditions

age = int(input("How old are you: ")) #storing user input in variable to be used later

if age <= 18:
    print("You are a youngin")
elif 18 < age < 31:
    print("You are livin life!")
else:   
    print("You are an unc")



#Practice 2, asking a user if they want some food:

eatingtime = input("Are you hungry? ")

if eatingtime == "yes":
    print("Eat some food big tubster")
else:
    print("Go drink some water sticky")
