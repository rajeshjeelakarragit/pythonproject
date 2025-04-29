class Parent1:
    def show(self):
        print("Parent1 method called.")

class Parent2:
    def display(self):
        print("Parent2 method called.")

class Child(Parent1, Parent2):
    pass

# Create an instance
child = Child()
child.show()
child.display()
