"""'7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens."""

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self.salary = salary
        self.__ssn = ssn

emp = Employee("John Doe", 50000, "123-45-6789")
print("Name" , emp.name) 
print("Salary" , emp.salary)

try:
    print("SSN" , emp.__ssn)  
except AttributeError as e:
    print("Error accessing private variable:", e)
print("SSN (with name mangling):", emp._Employee__ssn)
    