"""
The Factory pattern provides an interface for creating objects in a
superclass but allows subclasses to alter the type of objects that will be created.

"""

class AnimalFactory:
    @staticmethod
    def get_animal(type_):
        if type_ == "dog":
            return Dog()
        elif type_ == "cat":
            return Cat()
        else:
            return None

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Usage
animal = AnimalFactory.get_animal("dog")
print(animal.speak())  # Woof!
