# *args = allow you to pass multiple non-key arguments
# **kwargs = allow you to pass multiple key-value arguments
#     *unpacking operator


#ARGS

def add(*args): # *args = tuple, enbles me to add as many arguments as I want
    total =0
    for arg in args:
        total += arg
    return total
print(add(1, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("John", "Doe", "is", "a", "developer")


#KWARGS

def print_address(**kwargs): # **kwargs = dictionary, packs keyword argueemnts into a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Main St", city="Springfield", state="IL", zip="62701") #key = first word, value = second word


#Usign args and kwargs together

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("John", "Johnnyboy", "Johnathan", "III", #args
               street="123 Main St", #kwargs
               apt= "421",
               city="fakeville", 
               state="IL", 
               zip="62701") #kwargs

#args and kwargs can be used together, but args must come before kwargs

