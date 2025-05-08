import unittest

# Function to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test Case Class
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test addition
        self.assertEqual(add(-1, 1), 0)  # Test with negative numbers

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)  # Test subtraction
        self.assertNotEqual(subtract(10, 5), 6)  # Ensure wrong value fails

# Run tests
if __name__ == "__main__":
    unittest.main()


##############################
# pytestsample test_math_operations.py
# test_math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(10, 5) != 6
