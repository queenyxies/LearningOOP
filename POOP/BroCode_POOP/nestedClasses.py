# Nested class = A class defined within another class
#           class Outer:
#               class Inner:

# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           Keeps namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, employee_name, position):
            self.employee_name = employee_name
            self.position = position
        
        def get_details(self):
            return f"{self.employee_name} - {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    
    def add_employee(self, employee_name, position):
        # Create a new employee with the provided name and position
        new_employee = self.Employee(employee_name, position)
        # Add the employee to the list of employees
        self.employees.append(new_employee)

    def list_employees(self):
        # Print details of all employees
        if self.employees:
            for employee in self.employees:
                print(employee.get_details())
        else:
            print("No employees found.")

# Example usage
company = Company("Tech Solutions")
company.add_employee("Alice", "Developer")
company.add_employee("Bob", "Designer")

company.list_employees()
