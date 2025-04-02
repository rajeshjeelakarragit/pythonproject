#Basic Annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


#Multiple Parameters
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 10))  # Output: 15

#Annotations with Custom Types

from typing import List

def process_items(items: List[int]) -> List[int]:
    return [item * 2 for item in items]

print(process_items([1, 2, 3]))  # Output: [2, 4, 6]


#Using Annotations for Documentation
def greet(name: str = "Guest") -> "A friendly greeting message":
    return f"Hello, {name}!"

print(greet.__annotations__)
# Output: {'name': <class 'str'>, 'return': 'A friendly greeting message'}

#No Restrictions
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(3, "4"))  # Output: 444 (no type-checking is enforced)


#Accessing Annotations
def example(a: int, b: str) -> bool:
    return True

print(example.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'bool'>}


#Advanced Use Cases
#1. Type Aliases
from typing import List

Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

print(scale(2.0, [1.0, 2.0, 3.0]))
# Output: [2.0, 4.0, 6.0]

#2. Optional Types
from typing import Optional

def get_user(id: int) -> Optional[str]:
    return "User" if id == 1 else None

#3

def func_anno() -> int:
    result = "Hello, World"
    assert isinstance(result, int), f"Expected return type 'int', got {type(result)}"
    return result

print(func_anno())  # Will raise an assertion error
