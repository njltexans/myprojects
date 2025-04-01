# Practice credit card validator program (via python)

# 1) Remove any '-' or ' '
# 2) Add all digits in the odd places from right to left
# 3) Double every second digit from right to left
#       If result is 2 digit number, add 2 digit number together to get a single digit
# 4) Sum totals of steps 2 and 3
# 5) If the total is divisible by 10, the number is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1

card_number = input("Enter your credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")  # Remove any '-' or ' '
card_number = card_number[::-1] # Reverse the string (card number)

# Step 2

for i in card_number[::2]:
    sum_odd_digits += int(i)

# Step 3

for i in card_number[1::2]: # Double every second digit from right to left
    double = int(i) * 2  # Double the digit
    if double >= 10: # If result is 2 digit number, add 2 digit number together to get a single digit
        sum_even_digits += (1 + (double % 10)) 
    else: 
        sum_even_digits += double # Add the doubled digit to sum_even_digits

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0: # If the total is divisible by 10, the number is valid
    print("This is a valid credit card number.")
else:
    print("This is not a valid credit card number.")