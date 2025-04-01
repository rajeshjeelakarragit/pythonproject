"""
1. Basic Boolean Operations
"""
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True

"""
2. Checking Even or Odd Number
"""
num = 10
is_even = num % 2 == 0  # True if even, False if odd

print(is_even)  # Output: True

"""
3. Boolean with Comparison Operators
"""
x = 15
y = 20

print(x > y)   # False
print(x < y)   # True
print(x == y)  # False
print(x != y)  # True




"""
4. Boolean in Conditional Statements
"""
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

"""
5. Boolean with all() and any()
"""

values = [True, True, False]

print(all(values))  # False (all must be True)
print(any(values))  # True (at least one must be True)

"""
6. Checking If a String is Empty
"""
text = ""

is_empty = not bool(text)  # True if empty, False otherwise
print(is_empty)  # Output: True

"""
7. Using Boolean in a Function
"""
def is_positive(number):
    return number > 0

print(is_positive(5))  # True
print(is_positive(-3)) # False

"""
8. Boolean in List Comprehension
"""
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]

print(evens)  # Output: [2, 4, 6]

"""
9. Checking If a Number is in a List
"""
nums = [1, 2, 3, 4, 5]
print(3 in nums)   # True
print(10 in nums)  # False

"""
10. Boolean Short-Circuiting
"""
a = False and print("This won't print")  # Short-circuits
b = True or print("This won't print")   # Short-circuits

print(a, b)  # Output: False True
