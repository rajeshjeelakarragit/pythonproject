

"""
 1.
 Basic
 Float
 Operations
"""

a = 10.5
b = 2.3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor division (removes decimal part)
print(a % b)  # Modulus (remainder)
print(a ** b) # Exponentiation

"""
12.8
8.2
24.15
4.565217391304348
4.0
1.5999999999999996
177.97809317926652

"""

"""
2. Rounding a Float Number
"""

num = 3.14159
print(round(num, 2))  # Rounds to 2 decimal places


"""
3.14
"""

"""
3. Converting Integer to Float and Vice Versa
"""
int_num = 5
float_num = float(int_num)  # Convert integer to float
print(float_num)  # Output: 5.0

float_val = 5.7
int_val = int(float_val)  # Convert float to integer (truncates decimal part)
print(int_val)  # Output: 5


"""
4. Using math Library for Float Operations
"""
import math

x = 9.8

print(math.ceil(x))   # Rounds up (10)
print(math.floor(x))  # Rounds down (9)
print(math.sqrt(x))   # Square root
print(math.pi)        # Pi value


"""
10
9
3.1304951684997055
3.141592653589793

"""

"""
5. Checking If a Number is Float
"""
def is_float(value):
    return isinstance(value, float)

print(is_float(10.5))  # True
print(is_float(5))     # False

"""
6. Formatting Floats in Output
"""
num = 123.456789
print(f"Formatted to 2 decimal places: {num:.2f}")
print(f"Formatted to 4 decimal places: {num:.4f}")

"""
Formatted to 2 decimal places: 123.46
Formatted to 4 decimal places: 123.4568
"""

"""
7. Handling Float Division and Precision Errors
"""
result = 0.1 + 0.2
print(result)  # Due to floating-point precision, result may not be exactly 0.3
print(round(result, 1))  # Rounds to 0.3

"""
0.30000000000000004
0.3

"""

"""
8. Generating Random Float Numbers
"""
import random

print(random.uniform(1.5, 5.5))  # Generates a random float between 1.5 and 5.5


"""
9. Summing a List of Floats
"""
numbers = [1.2, 3.5, 4.8, 2.1]
print(sum(numbers))  # Output: 11.6

"""
10. Comparing Floating-Point Numbers Using math.isclose()
"""
import math

a = 0.1 + 0.2
b = 0.3

print(math.isclose(a, b, rel_tol=1e-9))  # True (compares within a small tolerance)



"""
"""


"""
"""