#Basic Class-Based Decorator
class GreetDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Hello!")
        self.func()
        print("Goodbye!")

@GreetDecorator
def say_name():
    print("My name is Alice.")

say_name()
'''
Hello!
My name is Alice.
Goodbye!

'''

# Class-Based Decorator with Parameters

class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper

@Repeat(3)
def greet():
    print("Hi!")

greet()
'''
Use class-based decorators when:

You need to store state across multiple calls

You want cleaner, organized code for complex logic

You're wrapping methods with extra functionality

'''