
"""14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object 
store a reference to an Employee object that exists independently of it."""
class Employee:
    def __init__(self, name):
        self.name = name
        
class Department:
    def __init__(self, department_name , employee):
       self.department_name = department_name
       self.employee = employee
    def show_details(self):
        return f"{self.employee.name} works in {self.department_name} department"
emp1 = Employee("Alice")

dep1 = Department("HR" , emp1)
print(dep1.show_details())  

