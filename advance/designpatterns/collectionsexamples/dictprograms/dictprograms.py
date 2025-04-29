#1. Create and Print a Dictionary

# Create a dictionary
person = {"name": "John", "age": 25, "city": "New York"}
print(person)
# Output: {'name': 'John', 'age': 25, 'city': 'New York'}

#2. Access and Modify Dictionary Elements
# Access values
print(person["name"])  # Output: John

# Modify values
person["age"] = 30
print(person["age"])  # Output: 30

# Add a new key-value pair
person["country"] = "USA"
print(person)
# Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

#3. Iterate Through a Dictionary

# Iterate through keys
for key in person:
    print(key)

# Iterate through values
for value in person.values():
    print(value)

# Iterate through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

#4. Check if a Key Exists
if "name" in person:
    print("Name exists")
else:
    print("Name does not exist")

# 5. Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)
# Output: {1: 'a', 2: 'b', 3: 'c'}

#6. Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: Using the `update()` method
dict1.update(dict2)
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Method 2: Using dictionary unpacking (Python 3.9+)
merged = {**dict1, **dict2}
print(merged)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#7. Delete Items from a Dictionary
# Remove a key-value pair
person.pop("age")
print(person)
# Output: {'name': 'John', 'city': 'New York', 'country': 'USA'}

# Remove the last key-value pair
person.popitem()
print(person)
# Output: {'name': 'John', 'city': 'New York'}

# Delete all items
person.clear()
print(person)
# Output: {}

#8. Count Word Frequencies
text = "apple banana apple orange banana apple"
words = text.split()

# Count frequencies
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}


#9. Sort a Dictionary by Keys or Values
# Sort by keys
sorted_by_keys = dict(sorted(squares.items()))
print(sorted_by_keys)

# Sort by values
sorted_by_values = dict(sorted(squares.items(), key=lambda item: item[1]))
print(sorted_by_values)

#10 Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

print(nested_dict["person1"]["name"])  # Output: Alice

