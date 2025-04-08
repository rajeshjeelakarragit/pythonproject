from abc import ABC, abstractmethod

class Animal:
     x=10

     def __new__(cls, *args, **kwargs):
         print("Creating instance")
         # Pass only the class type to super().__new__()
         instance = super().__new__(cls)
         return instance

     def __init__(self, name="default"):
         print("__init__ method is calling")
         self.name = name

     def speak(self):
         print("Animal is speaking")

     @staticmethod
     def speak12():
         print("I am speaking!")

     def __str__(self):
        return f"Employee(name={self.name})"

     @abstractmethod
     def display(self):
         pass


class Dog:
    def display(self):
        print("dog display")

animal = Animal("cog")
print(animal.x)
animal.speak()
Animal.speak12()
print(Animal("cog"))

dog = Dog()
dog.display()