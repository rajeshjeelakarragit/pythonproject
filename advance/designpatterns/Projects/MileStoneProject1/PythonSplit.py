text = "Python is awesome"
result = text.split()
print(result)  # Output: ['Python', 'is', 'awesome']

text = "apple,banana,orange"
result = text.split(',')
print(result)  # Output: ['apple', 'banana', 'orange']

text = "apple,banana,orange"
result = text.split(',', 1)  # Split only once
print(result)  # Output: ['apple', 'banana,orange']


text = "Hello\nWorld\nPython"
result = text.splitlines()
print(result)  # Output: ['Hello', 'World', 'Python']

import re

text = "apple, banana; orange|grape"
result = re.split('[,;|]', text)
print(result)  # Output: ['apple', ' banana', ' orange', 'grape']