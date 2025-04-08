class Department:


    'Common base class for all Department'
    empCount = 2
    name = "Bhavesh Aggarwal"
    age = "30"

    # Class attribute
    price = 4000

    def __init__(self, name):
        self.name = name


    def display(self):
        print(self)
        print("Total Employee %s" % self.name)

    def showcount(self):
        print(self.empCount)

    counter = classmethod(showcount)


    @classmethod
    def showcount(cls):
        print(cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

    @classmethod
    def showPrice(cls):
        return cls.price

    # class method
@classmethod
def brandName(cls):
  print("Name of the brand is Raymond")

print()
print('Access class or static variable' , Department.empCount)
department = Department('tcs')
department.display()
Department.counter()

# Accessing class attribute
print(Department.showPrice())

# adding dynamically
setattr(Department, "brand_name", brandName)
newObj = Department()
newObj.brand_name()

