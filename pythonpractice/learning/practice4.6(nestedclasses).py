# Nested class = A class defined within another class 
#       - Class outer
#           - Class inner

# Benefits of this is that it allows you to logically group classes that are closely related
#       - Encapsulate private details that aren't relevant outside of outer class
#       - Keeps namespace clean
#       - Reduces possibility of naming conflicts

class company: # Outer class of the nested class
    class employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} is a {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company1 = company("Google (Noah's Version)")

company1.add_employee("Noah", "Software Engineer")
company1.add_employee("Squidward", "Cashier")

company2 = company("Microsoft (Noah's Version)")

company2.add_employee("Noah Jr.", "Software Engineer")
company2.add_employee("Patrick", "Janitor")

for employee in company2.list_employees():
    print(employee)





class nonprofit: # Outer class of the nested class
    class employee:
        pass




