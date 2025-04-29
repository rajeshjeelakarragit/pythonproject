"""
Using Abstract Base Classes
Import the abc module.
Define an abstract class by inheriting from abc.ABC.
Use the @abstractmethod decorator to mark methods that subclasses must implement.
"""
from abc import ABC, abstractmethod

# Define an interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Implement the interface in a concrete class
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Run on four legs"


class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def move(self):
        return "Fly"

# Usage
animals = [Dog(), Bird()]
for animal in animals:
    print(f"{animal.speak()} - {animal.move()}")