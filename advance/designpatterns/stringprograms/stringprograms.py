# Assign s as a string
s = 'Hello World'

# Print the object
print(s)

# Show first element (in this case a letter)
s[0]

s[1]

# Grab everything past the first term all the way to the length of s which is len(s)
s[1:] # 'ello World'


# Grab everything UP TO the 3rd index
s[:3]


#Everything
print(s[:])

# Last letter (one index behind 0 so it loops back around)
print(s[-1])

# Grab everything but the last letter
 # 'Hello Worl'

print(s[:-1])

# Grab everything, but go in steps size of 1
 # 'Hello World'
print(s[::1])

# Grab everything, but go in step sizes of 2
 #'HloWrd'
print(s[::2])

# We can use this to print a string backwards
print(s[::-1] )# 'dlroW olleH'
# Concatenate strings!
print(s + ' concatenate me!')

# We can reassign s completely though!
s = s + ' concatenate me!'

print(s)

letter = 'z'
print(letter*10)


# Upper Case a string
s.upper()

print(s)

# Lower case
s.lower()
#

print(s)

# Split a string by blank space (this is the default)
s.split()

#['Hello', 'World', 'concatenate', 'me!']

# Split by a specific element (doesn't include the element that was split on)
s.split('W') # ['Hello ', 'orld concatenate me!']

['Hello', 'World', 'concatenate', 'me!']
#['Hello ', 'orld concatenate me!']




'Insert another string with curly brackets: {}'.format('The inserted string')
#'Insert another string with curly brackets: The inserted string'