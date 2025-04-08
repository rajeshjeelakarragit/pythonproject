class Bird:
    def fly(self):
        print("Bird is flying.")

class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly but can swim.")

# Polymorphism in action
def perform_fly(bird):
    bird.fly()

sparrow = Bird()
penguin = Penguin()

perform_fly(sparrow)
perform_fly(penguin)
