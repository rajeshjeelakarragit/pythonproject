class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)


# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


# Add an 'age' attribute
emp1.age = 7
# Modify 'age' attribute
emp1.age = 8
# Delete 'age' attribute
del emp1.age

# Returns true if 'age' attribute exists
hasattr(emp1, 'age')
# Returns value of 'age' attribute
getattr(emp1, 'age')
# Set attribute 'age' at 8
setattr(emp1, 'age', 8)
# Delete attribute 'age'
delattr(emp1, 'age')

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)