# Exception Handling
# An exception is an event that dusrupts the normal flow of a program.
# Some examples:
#   - (ZeroDivisionError, TypeError, ValueError, FileNotFoundError, IndexError)
#   - 1) Try, 2) Except, 3) Finally
#   - Try: The code that might cause an exception.
#   - Except: The code that runs if an exception occurs.
#   - Finally: The code that runs no matter what.


try: # Try block, code that might cause an exception
    number = int(input("Enter a number: "))
    print(1/number)

except ZeroDivisionError: # Catching a specific exception, ZeroDivisionError
    # This exception occurs when dividing by zero
    print("You can't divide by zero!")

except ValueError: # Catching a specific exception, ValueError
    # This exception occurs when the input cannot be converted to an integer
    print("That's not a valid number!")

except Exception: # Catching any other exception
    # This is a generic exception handler that catches all exceptions
    # It's a good practice to use this as a last resort
    print("An unexpected error occurred.")

finally: # Finally block, code that runs no matter what
    # This block will always run, regardless of whether an exception occurred or not
    # It's often used for cleanup actions or final messages
    print("This will always run.")