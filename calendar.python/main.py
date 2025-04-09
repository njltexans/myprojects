def is_leap_year(year): #Check if we have leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year): #Get days in month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError("Invalid month")
    

def get_first_day_of_month(month, year): #Get first day of month
    if month < 3: #Zeller's congruence
        month += 12
        year -= 1
    q = 1
    k = year % 100
    j = year // 100
    h = (q + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return (h + 5) % 7

def print_cal(month, year): #Print calendar
    month_name = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
    days_in_month = get_days_in_month(month, year)
    first_day = get_first_day_of_month(month, year)
    print(f"{month_name[month - 1]} {year}".center(20))
    print("Mon Tue Wed Thu Fri Sat Sun")
    for _ in range(first_day):
        print("    ", end="")
    for day in range(1, days_in_month + 1):
        print(f"{day:3} ", end="")
        first_day = (first_day + 1) % 7
        if first_day == 0:
            print()
    print()

month = int(input("Enter Month (1-12): "))
year = int(input("Enter Year: "))
print_cal(month, year)