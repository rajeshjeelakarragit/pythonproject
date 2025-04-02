def sample():
    print("Hello, this is first sample function")

#sample()

def sample(name:str):
    print(f"{name}, this is first sample function")

#sample(1)


#Using Annotations for Documentation
def greet(name: str = "Guest") -> "A friendly greeting message":
    return f"Hello, {name}!"

print(greet.__annotations__)
# Output: {'name': <class 'str'>, 'return': 'A friendly greeting message'}