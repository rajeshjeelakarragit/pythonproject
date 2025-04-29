from abc import ABC, abstractmethod


# Define an abstract class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Sleeping...")


# Concrete class inheriting from the abstract class
class Dog(Animal):

    def make_sound(self):
        print("Bark!")


# Another concrete class
class Cat(Animal):

    def make_sound(self):
        print("Meow!")


# Attempting to instantiate an abstract class raises an error
# animal = Animal()  # This will raise TypeError

# Instantiate concrete classes
dog = Dog()
dog.make_sound()  # Output: Bark!
dog.sleep()  # Output: Sleeping...

cat = Cat()
cat.make_sound()  # Output: Meow!
cat.sleep()  # Output: Sleeping...
