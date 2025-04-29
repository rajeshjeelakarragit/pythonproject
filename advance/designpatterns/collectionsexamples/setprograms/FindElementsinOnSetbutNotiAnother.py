set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

unique_to_set1 = set1.difference(set2)
unique_to_set2 = set2.difference(set1)

print("Unique to set1:", unique_to_set1)
print("Unique to set2:", unique_to_set2)
"""
Unique to set1: {1, 2}
Unique to set2: {5, 6}
"""