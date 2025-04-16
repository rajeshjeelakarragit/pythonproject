class MyCustomError(Exception):
    """Custom exception for specific error."""
    pass

def divide(a, b):
    if b == 0:
        raise MyCustomError("Denominator cannot be zero!")
    return a / b

try:
    print(divide(10, 0))
except MyCustomError as e:
    print("Caught custom error:", e)
