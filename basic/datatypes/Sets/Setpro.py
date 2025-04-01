numbers = {10,11,12,13}

for num in numbers:
    print(num)

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

#Adding Elements to a Set

my_set = {1, 2, 3}
my_set.add(4)  # Add a single element
print(my_set)  # Output: {1, 2, 3, 4}

#Removing Elements from a Set

my_set = {1, 2, 3, 4, 5}

my_set.remove(3)  # Removes 3 (raises error if not found)
print(my_set)  # Output: {1, 2, 4, 5}

my_set.discard(2)  # Removes 2 (does not raise error if not found)
print(my_set)  # Output: {1, 4, 5}

my_set.pop()  # Removes and returns a random element
print(my_set)  # Output varies


#Set Operations (Union, Intersection, Difference, Symmetric Difference)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)  # Union: {1, 2, 3, 4, 5, 6}
print(set1 & set2)  # Intersection: {3, 4}
print(set1 - set2)  # Difference: {1, 2} (Elements in set1 but not in set2)
print(set1 ^ set2)  # Symmetric Difference: {1, 2, 5, 6} (Elements not in both)



#Checking for Element Existence
my_set = {1, 2, 3, 4, 5}

print(3 in my_set)   # Output: True
print(6 in my_set)   # Output: False


# Iterating Through a Set

my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)  # Output: Items in random order

#Finding Length of a Set
my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5

# Converting List to Set (Removing Duplicates)
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)  # Converts list to set, removing duplicates
print(my_set)  # Output: {1, 2, 3, 4, 5}

#Set Subset and Superset
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

print(setA.issubset(setB))  # Output: True (setA is inside setB)
print(setB.issuperset(setA))  # Output: True (setB contains setA)

#Frozen Set (Immutable Set)
# Creating a frozen set
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # Output: frozenset({1, 2, 3, 4})

# Trying to modify it will raise an error
# frozen.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'


