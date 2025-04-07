# default arguments = a default value for specific parameters 
# default is used when that argument is ommitted 
# making your functions more flexible reduces the number of aurguemnts you need to pass in

def net_price(list_price, discount=0, tax=.13): #if discount and tax are constant you can set these as default arguments and edit the price as needed
    return list_price * (1- discount) * (1+ tax)

print(net_price(550))
# You can also pass in new arguments to override the default arguments when relevant
#example:
print(net_price(550, .15)) #this will change the discount to 15%

# You need to make sure any default arguments are placed after any non-default arguments (ones that are being passed in)




