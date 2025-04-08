class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"This is a {cls.__name__} class."

# Usage
print(MathOperations.add(10, 20))
print(MathOperations.description())
