# multithreading is used to perform multiple tasks at once 
#   -  It is good for I/O bound tasks (waiting for input/output) such as reading files, or fetching data from apis
#   -  It is not good for CPU bound tasks (processing data) such as calculations
#   -  threading.thread(target=target_function) is used to create a new thread


import threading
import time

#Doing multiple chores

def walk_dog(pet_name): # function to walk the dog
    time.sleep(8) # simulating a delay of 8 seconds (amount of time it takes to walk the dog)
    print(f"You finished walking {pet_name}")

def take_out_trash(): # function to take out the trash
    time.sleep(2) # simulating a delay of 2 seconds (amount of time it takes to take out the trash)
    print("You took out the trash")

def get_mail(): # function to get the mail
    time.sleep(5) # simulating a delay of 5 seconds (amount of time it takes to get the mail)
    print("You got the mail")


chore1 = threading.Thread(target=walk_dog, args=("Fido",)) # creating a thread for walking the dog, passing the pet name as an argument (adding coma to make it a tuple)
chore1.start() # starting the thread for walking the dog


chore2 = threading.Thread(target=take_out_trash) # creating a thread for taking out the trash
chore2.start() # starting the thread for taking out the trash

chore3 = threading.Thread(target=get_mail) # creating a thread for getting the mail
chore3.start() # starting the thread for getting the mail
# The main thread will continue to run while the other threads are running

chore1.join() # This will block the main thread until chore1 is completed
chore2.join() # This will block the main thread until chore2 is completed
chore3.join() # This will block the main thread until chore3 is completed

print("All chores are completed!") # This will print after all the threads are started