"""
The Decorator pattern allows behavior to be added to an individual object, dynamically.
"""

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello!")

# Usage
say_hello()
