class EmployeeConstructor:
   'Common base class for all employees'
   #def __init__(self):
    #  self.name = "Bhavana"
    #  self.age = 24


   def __init__(self, name=None, age=None):
       if name and age:
           self.name = name
           self.age = age
       elif name:
           self.name = name
           self.age = "Unknown"
       else:
           self.name = "Unknown"
           self.age = "Unknown"

# e1 = EmployeeConstructor()
# print ("Name: {}".format(e1.name))
# print ("age: {}".format(e1.age))

e1 = EmployeeConstructor("Bhavana", 24)
e2 = EmployeeConstructor("Bharat", 25)


print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))