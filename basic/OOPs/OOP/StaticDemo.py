class StaticDemo:
    empCount = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        StaticDemo.empCount += 1

    # creating static method using staticmethod() function
    def showcount():
        print(StaticDemo.empCount)

    counter = staticmethod(showcount)
    # assigning static method using staticmethod()

    @staticmethod
    def showcount(a, b):
        return a + b

# Creating instances of StaticDemo
e1 = StaticDemo("Bhavana", 24)
e2 = StaticDemo("Rajesh", 26)
e3 = StaticDemo("John", 27)

# Calling the static method
e1.counter()  # Can be called through an instance
StaticDemo.counter()  # Or through the class
print(StaticDemo.showcount(1,2))
