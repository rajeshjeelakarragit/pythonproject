class Employee:

    def __new__(cls, *args , **kwargs):
        print("Creating instance")
        # Pass only the class type to super().__new__()
        instance = super().__new__(cls)
        return instance

    def __init__(self , name , age):
        print("Initializing instance")
        self.__name = name
        self.__age = age
        self._salary=2000

    def __str__(self):
        return f"Employee(name={self.__name})"


print(Employee("Shashi" , 20))

employee = Employee("Shashi" , 40)
print(f"Employee name {employee._salary}")