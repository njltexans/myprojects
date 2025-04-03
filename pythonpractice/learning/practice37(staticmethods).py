# Static metjods are methods that belong to a class rather than any object from that class (instance)
#       - Used for general utility functions that do not need to access any instance specific data

# Instance methods are best for operations on instances of the class (objects)
# Static methods are best for operations that do not need to access any instance specific data


class employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_informtion(self):
        return f"{self.name} is the {self.position}"
    
    @staticmethod
    def isvalid_position(position): # Static method 
        valid_positions = ["Manager", "Assistant Manager", "Cashier", "Cook", "King of the Cooks"] # List of valid positions
        return position in valid_positions # Returns True if the position is valid, False otherwise
    

employee1 = employee("Squidward", "Cashier")
employee2 = employee("Spongebob", "Cook")
employee3 = employee("Walter White", "King of the Cooks")

print(employee.isvalid_position("Manager")) # Checking to see if "manager" is a valid position
print(employee3.get_informtion()) # Getting the information of employee3
