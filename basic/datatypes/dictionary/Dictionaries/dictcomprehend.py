"""
{key_expression: value_expression for item in iterable if condition}
"""

"""
Example 1: Creating a dictionary from a list
"""

numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print(squares)

"""
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

"""
Example 2: Filtering elements in dictionary comprehension
"""
numbers = range(10)
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares)

"""
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
"""

"""
Example 3: Swapping keys and values in a dictionary
"""
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)


"""
{1: 'a', 2: 'b', 3: 'c'}
"""

"""
1. Creating a Dictionary from Two Lists
"""

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

person = {k: v for k, v in zip(keys, values)}
print(person)
"""
{'name': 'Alice', 'age': 25, 'city': 'New York'}
"""

"""
2. Using Conditional Logic in Dictionary Comprehension
"""
numbers = range(10)
odd_squares = {num: num**2 for num in numbers if num % 2 != 0}
print(odd_squares)

"""
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
"""


"""
3. Transforming Dictionary Values
"""
grades = {'Alice': 85, 'Bob': 78, 'Charlie': 92}

curved_grades = {k: v + 5 for k, v in grades.items()}
print(curved_grades)


"""
{'Alice': 90, 'Bob': 83, 'Charlie': 97}
"""

"""
4. Filtering a Dictionary
"""

grades = {'Alice': 85, 'Bob': 78, 'Charlie': 92, 'David': 60}
passed_students = {k: v for k, v in grades.items() if v >= 80}

print(passed_students)

"""
{'Alice': 85, 'Charlie': 92}
"""

"""
5. Nesting Dictionary Comprehensions
"""

students = ['Alice', 'Bob', 'Charlie']
scores = {student: {subject: 0 for subject in ['Math', 'Science', 'English']} for student in students}

print(scores)


"""
{
    'Alice': {'Math': 0, 'Science': 0, 'English': 0},
    'Bob': {'Math': 0, 'Science': 0, 'English': 0},
    'Charlie': {'Math': 0, 'Science': 0, 'English': 0}
}

"""
"""
6. Counting Character Frequency in a String
"""

text = "hello world"
char_count = {char: text.count(char) for char in set(text) if char != ' '}
print(char_count)

"""
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

"""
7. Creating a Dictionary with Enumerate
"""

fruits = ['apple', 'banana', 'cherry']
fruit_dict = {index: fruit for index, fruit in enumerate(fruits, start=1)}
print(fruit_dict)

"""
{1: 'apple', 2: 'banana', 3: 'cherry'}
"""