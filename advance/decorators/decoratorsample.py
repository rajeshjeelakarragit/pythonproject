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