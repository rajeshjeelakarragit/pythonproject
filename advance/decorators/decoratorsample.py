#Basic Decorator Example
def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greet_decorator
def say_name():
    print("My name is Alice.")

say_name()
'''
Hello!
My name is Alice.
Goodbye!
'''
decorated_func = greet_decorator(say_name)
decorated_func()

#Decorator with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

'''
Hello!
Hello!
Hello!

'''

# Real-World Example: Logging Decorator
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(x, y):
    return x + y

add(10, 20)
'''
Calling add with (10, 20) and {}
add returned 30

'''


def dec_func(org_func):
    print("hello dec func")

    def war(*args , **kwargs):
        return org_func(*args , **kwargs)
    return war



@dec_func
def ext_func(a , b=None , c="hello123"):
    print(f"this is need to be dec {a}  {b}  {c}")
    return a + b

name = 'mahesh'
last = 'p'
result = ext_func(name , last , c="hel")
print(result)


def my_decorator(func):
    def wrapper(name, last, a="hello", *args, **kwargs):
        # Pre-function behavior
        print(f"Calling {func.__name__} with arguments: name={name}, last={last}, a={a}")
        print(f"Additional args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = func(name, last, a, *args, **kwargs)

        # Post-function behavior
        print(f"{func.__name__} returned: {result}")

        return result
    return wrapper


@my_decorator
def ext_func(name, last, a="hello"):
    return f"{a}, {name} {last}!"

result = ext_func("John", "Doe", a="Hi")
print(result)

"""
# Call the function
result = ext_func("John", "Doe", a="Hi")
print(result)

# Output:
# Calling ext_func with arguments: name=John, last=Doe, a=Hi
# Additional args: (), kwargs: {}
# ext_func returned: Hi, John Doe!
# Hi, John Doe!
"""

'''
Use Cases for Decorators
Logging

Authentication

Memoization (caching)

Timing function execution

Access control

Retry mechanisms

'''