numbers = (10,11,12,13)

for num in numbers:
    print(num)

# Creating a tuple
my_tuple = (1, 2, 3, "Hello", 4.5)
print(my_tuple)  # Output: (1, 2, 3, 'Hello', 4.5)


# Accessing elements using indexing
my_tuple = (10, 20, 30, 40)

print(my_tuple[0])  # Output: 10
print(my_tuple[-1]) # Output: 40 (Last element)


# Slicing a tuple
numbers = (1, 2, 3, 4, 5, 6)

print(numbers[1:4])  # Output: (2, 3, 4)
print(numbers[: 3])   # Output: (1, 2, 3)
print(numbers[::2])  # Output: (1, 3, 5) (Skipping elements)


# Unpacking a tuple
person = ("Alice", 25, "Engineer")

name, age, profession = person

print(name)       # Output: Alice
print(age)        # Output: 25
print(profession) # Output: Engineer

# Concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)

result = t1 + t2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
t3 = ("Hi",) * 3
print(t3)  # Output: ('Hi', 'Hi', 'Hi')

# Using 'in' keyword
my_tuple = ("apple", "banana", "cherry")

print("banana" in my_tuple)  # Output: True
print("grape" in my_tuple)   # Output: False

numbers = (10, 20, 30, 40, 50)

print(len(numbers))  # Output: 5
print(min(numbers))  # Output: 10
print(max(numbers))  # Output: 50

# Converting list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# Converting tuple to list
my_new_list = list(my_tuple)
print(my_new_list)  # Output: [1, 2, 3]

# A tuple with a single element requires a comma!
single_element_tuple = (5,)  # Correct
not_a_tuple = (5)            # This is just an integer

print(type(single_element_tuple))  # Output: <class 'tuple'>
print(type(not_a_tuple))           # Output: <class 'int'>

# Function returning a tuple
def get_coordinates():
    return (10.5, 20.8)

x, y = get_coordinates()
print(f"X: {x}, Y: {y}")  # Output: X: 10.5, Y: 20.8
