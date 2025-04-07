# variable scope is when a variable is visible and accessible 
# scope resolution = (LEGB) Local, Enclosing, Global, Built-in (this is the order of operations python looks for a variable definition)



def func1():
    x = 10
    print(x)

def func2():
    x=5
    print(x)


func1() 
func2()
# the x in func1 is different from the x in func2
# this is because the x in func1 is local to func1
# and the x in func2 is local to func2


