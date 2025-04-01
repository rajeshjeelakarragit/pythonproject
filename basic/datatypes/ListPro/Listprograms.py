#Example 1: Using sort()

# In-place sorting
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Ascending order
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]


#Example 2: Using sorted()
# Creating a new sorted list
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Ascending order
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]

# Original list remains unchanged
print(numbers)  # Output: [5, 2, 9, 1, 5, 6]

# Descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [9, 6, 5, 5, 2, 1]

#Example: Custom Sorting with key
# List of strings
words = ["apple", "banana", "kiwi", "cherry"]

# Custom sort by length of the string - Sort by String Length
words.sort(key=len)
print(words)  # Output: ['kiwi', 'apple', 'cherry', 'banana']

#Sort by a Computed Value

# List of numbers
numbers = [1, 12, 5, 111, 22]

# Custom sort by the remainder when divided by 10
numbers.sort(key=lambda x: x % 10)
print(numbers)  # Output: [111, 1, 12, 22, 5]


#Example: Using sorted() with a Custom Key
# Original list
numbers = [1, 12, 5, 111, 22]

# Create a new sorted list based on the square of the numbers
sorted_numbers = sorted(numbers, key=lambda x: x**2)
print(sorted_numbers)  # Output: [1, 5, 12, 22, 111]


#Advanced Example: Custom Sort Using a Function

# Define custom sorting function
def custom_key(x):
    return abs(x - 50)  # Sort by proximity to 50

# List of numbers
numbers = [10, 70, 30, 50, 40]

# Apply custom sort
numbers.sort(key=custom_key)
print(numbers)  # Output: [50, 40, 30, 70, 10]


#Custom Sorting for Complex Data (e.g., List of Dictionaries)

# List of dictionaries
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 23},
]

# Sort by age
students.sort(key=lambda student: student["age"])
print(students)
# Output: [{'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
