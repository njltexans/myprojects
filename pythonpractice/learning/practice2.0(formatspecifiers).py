# format specifiers = {value:flags} format a value based on the flags inserted

# .(number)f = round to the number of decimal places
# :(number) = allocate that many spaces 
#:03 = allocate 3 spaces
# :< = left align
# :> = right align
# :^ = center align
# :_ = fill with underscores
# :0 = fill with zeroes
# :+ = use plus sign for positive numbers
# :- = use minus sign for negative numbers
# :, = use comma as a thousand separator
# := = use the equal sign at the beginning of the number

price1 = 3.6782
price2 = -978.62
price3 = 12.45

print(f"Price 1 is {price1:.1f}") #: number of decimals and then f 
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")


