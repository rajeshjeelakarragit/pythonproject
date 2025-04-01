capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}


d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

# Creating a dictionary using curly braces
sports_player = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)


student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)

# Accessing values using the get() method
age = student_info.get("age")
print("Age:",age)

# Default value provided if key is not found
grad_year = student_info.get("graduation_year", "2023")

# Accessing all keys using the keys() method
all_keys = student_info.keys()
print("Keys:", all_keys)

# Accessing all values using the values() method
all_values = student_info.values()
print("Values:", all_values)

# Modifying an existing key-value pair
student_info["age"] = 22

# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)

# Adding a new key-value pair 'city': 'New York'
student_info.setdefault('city', 'New York')

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Updating multiple values
person.update({'age': 26, 'city': 'Los Angeles'})
print(person)

# Removing an item using the del statement
del student_info["major"]

# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")

# Removing the last key-value pair
removed_item = person.popitem()

print(student_info)

numbers.clear()

# Removing items based on conditions
keys_to_remove = ["age", "major"]
for key in keys_to_remove:
    student_info.pop(key, None)

print(student_info)

# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])

# Iterating through values
for value in student_info.values():
   print("Values:",value)

# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value)


marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)


newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)

marks |= marks1
print ("marks dictionary after update: \n", marks)

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.items()


original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
shallow_copy = original_dict.copy()

# Modifying the shallow copy
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")

print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)

original_dict = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
shallow_copy = dict(original_dict)

# Modifying the shallow copy
shallow_copy["age"] = 31
shallow_copy["skills"].append("C#")

print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)

import copy

original_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "education": {
      "degree": "Bachelor's",
      "field": "Computer Science"
   }
}

# Creating a deep copy
deep_copy = copy.deepcopy(original_dict)

# Modifying the deep copy
deep_copy["age"] = 26
deep_copy["skills"].append("Machine Learning")
deep_copy["education"]["degree"] = "Master's"

# Retrieving both dictionaries
print("Original dictionary:", original_dict)
print("Deep copy:", deep_copy)


# Creating a dictionary
dict1 = {"name": "Krishna", "age": "27", "doy": 1992}

# Copying the dictionary
dict2 = dict1.copy()

# Printing both of the dictionaries
print("dict1 :", dict1)
print("dict2 :", dict2)

# Define the outer dictionary
nested_dict = {
   "outer_key1": {"inner_key1": "value1", "inner_key2": "value2"},
   "outer_key2": {"inner_key3": "value3", "inner_key4": "value4"}
}
print(nested_dict)


# Define an empty outer dictionary
nested_dict = {}

# Add key-value pairs to the outer dictionary
outer_keys = ["outer_key1", "outer_key2"]
for key in outer_keys:
   nested_dict[key] = {"inner_key1": "value1", "inner_key2": "value2"}
print(nested_dict)

# Initial nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"}
}

# Adding a new key-value pair to Alice's nested dictionary
students["Alice"]["GPA"] = 3.8

# Adding a new nested dictionary for a new student
students["Charlie"] = {"age": 22, "major": "Mathematics"}

print(students)

# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Access Alice's major
alice_major = students["Alice"]["major"]
print("Alice's major:", alice_major)

# Access Bob's age
bob_age = students["Bob"]["age"]
print("Bob's age:", bob_age)


# Access Alice's major using .get()
alice_major = students.get("Alice", {}).get("major", "Not Found")
print("Alice's major:", alice_major)

# Safely access a non-existing key using .get()
dave_major = students.get("Dave", {}).get("major", "Not Found")
print("Dave's major:", dave_major)

# Delete the dictionary for Bob
del students["Bob"]

# Print the updated nested dictionary
print(students)


# Iterating through the Nested Dictionary:
for student, details in students.items():
   print(f"Student: {student}")
   for key, value in details.items():
      print(f"  {key}: {value}")