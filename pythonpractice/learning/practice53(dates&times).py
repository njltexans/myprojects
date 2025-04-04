 # Working with dates and times in Python

import datetime

date = datetime.date(2023, 10, 1) #Access datetime module, then pass in the year, month, and day

today = datetime.date.today() #Get today's date

time = datetime.time(12, 30, 45) #Access time module, then pass in the hour, minute, and second

now = datetime.datetime.now() #Get the current date and time

now = now.strftime("%Y-%m-%d %H:%M:%S") #Format the current date and time %Y is the year, %m is the month, %d is the day, %H is the hour, %M is the minute, and %S is the second
#Format the current date and time

target_datetime = datetime.datetime(2023, 10, 1, 12, 30, 45) #Access datetime module, then pass in the year, month, day, hour, minute, and second
target_datetime = target_datetime.strftime("%Y-%m-%d %H:%M:%S") #Format the target date and time
#Format the target date and time

print(date, today, time, now) #Print the date, today's date, time, and current date and time