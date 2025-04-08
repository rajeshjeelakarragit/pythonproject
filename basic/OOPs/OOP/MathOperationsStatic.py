class MathOperationsStatic:
    # Static method to add two numbers
    @staticmethod
    def add_numbers(a, b):
        return a + b

# Using the static method without creating an instance of the class
result = MathOperationsStatic.add_numbers(5, 10)
print("The sum is:", result)
