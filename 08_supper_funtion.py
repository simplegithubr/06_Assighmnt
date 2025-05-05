"""8. The super() Function
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class
 Teacher from it, add a subject field, and use super() to call the base class constructor."""

class Person:
    def __init__(self, name):
        self.name = name
        
class  Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the parent class
        self.subject = subject
        
t = Teacher("Alice", "Math")
print("Name" , t.name)  # Output: Alice
print("subject" ,t.subject)  # Output: Math
    