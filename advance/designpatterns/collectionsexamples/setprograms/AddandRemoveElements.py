my_set = {1, 2, 3}

# Add elements
my_set.add(4)
print("After adding 4:", my_set)

# Remove an element
my_set.remove(2)
print("After removing 2:", my_set)

# Discard (no error if the element doesn't exist)
my_set.discard(5)
print("After discarding 5:", my_set)

# Pop a random element
removed_element = my_set.pop()
print(f"Removed: {removed_element}, Remaining Set: {my_set}")

"""
After adding 4: {1, 2, 3, 4}
After removing 2: {1, 3, 4}
After discarding 5: {1, 3, 4}
Removed: 1, Remaining Set: {3, 4}

"""
