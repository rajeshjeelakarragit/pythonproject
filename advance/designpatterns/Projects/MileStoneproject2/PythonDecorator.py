def new_decorator(original_func):

    def wrap_func():
        print("Some extra code , before the original function")
        original_func()
        print("Some extra code , after the original function")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be a decorator")

#func_needs_decorator() # I want to be a decorator

#decoratored_fun = new_decorator(func_needs_decorator)

#print(decoratored_fun)

#func_needs_decorator()

"""
Some extra code , before the original function
I want to be a decorator
Some extra code , after the original function

"""

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

# Equivalent to: say_hello = decorator(say_hello)

#say_hello()

#

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice", 30)

"""
Arguments passed: ('Alice', 30), {}
Hello, Alice. You are 30 years old.
"""

# Decorating Functions That Return Values

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling the function...")
        result = func(*args, **kwargs)
        print("Function executed.")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

result = add(5, 7)
print(f"Result: {result}")

"""
Calling the function...
Function executed.
Result: 12
"""

#Decorators with Arguments
def decorator_with_args(prefix):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Before the function call")
            result = func(*args, **kwargs)
            print(f"{prefix}: After the function call")
            return result
        return wrapper
    return actual_decorator

@decorator_with_args("DEBUG")
def multiply(a, b):
    return a * b

print(multiply(3, 4))

"""
DEBUG: Before the function call
DEBUG: After the function call
12

"""

#Built-in Decorators

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = MyClass(10)
print(obj.value)  # Accessing the property
obj.value = 20    # Setting a new value
print(obj.value)
