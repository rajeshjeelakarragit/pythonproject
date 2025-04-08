class Animal:

    def __init__(self, name):
        self.rajesh = name
        self.language=''


    def sound(self):
        print(f"{self.rajesh} makes a sound.")

class Dog(Animal):

    def sound(self):
        print(f"{self.rajesh} barks.")

# Create instances

animal = Animal("Generic Animal")
dog = Dog("Buddy")

animal.sound()
dog.sound()

"""
Generic Animal makes a sound.
Buddy barks.
"""