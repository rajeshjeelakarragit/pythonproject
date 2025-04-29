#[expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

number = [num for num in range(10)]
print(number)

#Apply a Transformation
# Double each number in a list
nums = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in nums]
print(doubled)  # Output: [2, 4, 6, 8, 10]

#4. Nested Loops in List Comprehension
# Generate all pairs (x, y) where x is from 1-3 and y is from 4-6
pairs = [(x, y) for x in range(1, 4) for y in range(4, 7)]
print(pairs)  # Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

#5. Flatten a Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]


#6. Conditional Transformation
# Replace even numbers with "Even" and odd numbers with "Odd"
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

#7. Create a Dictionary from a List
# Generate a dictionary with numbers as keys and their squares as values
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
