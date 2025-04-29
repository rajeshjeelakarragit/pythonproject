# Create a frozenset
fs = frozenset([1, 2, 3, 4])

# Frozen set cannot be modified
print("Frozen Set:", fs)

# Membership test works
print(3 in fs)  # True

# Union operation
print("Union with {3, 5}:", fs | {3, 5})

"""
Frozen Set: frozenset({1, 2, 3, 4})
True
Union with {3, 5}: frozenset({1, 2, 3, 4, 5})
"""
