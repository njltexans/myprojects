# Recursion is a function that calls itself from within its own definition.
#   - helps to visualize a complex problem into basic steps which can be solved more easily iteratively or recursively.
#   - can be used to solve problems that can be broken down into smaller subproblems.


# Iterative approach

def walk(steps):
        for step in range(1, steps + 1):
            print(f"Step {step} taken.")

walk(5)

# Recursive approach

def walk(steps):
    if steps == 0:
        return
    else:
        walk(steps - 1)
        print(f"Step {steps} taken.")
walk(5)
# Recursion is a function that calls itself from within its own definition.

# Iterative approach 2

def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result
print(factorial(5))

# Recursive approach 2
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(5))