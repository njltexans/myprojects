# module is a file code you want to include in your program
# use 'import' to include a module (built in or your own)
#great for breaking up a large program into smaller, more manageable pieces

help('modules') # lists all the modules in the standard library

print(help('random')) # gives information about the random module, can replace random with different module to get info/functions of module

import math as m # imports the math module and gives it the alias m, can change m to any name you want

from math import sqrt # imports the sqrt function from the math module, can use to import specific functions from a module  

result= m.sqrt(16) # uses the sqrt function from the math module to find the square root of 16, can use this for others as well
