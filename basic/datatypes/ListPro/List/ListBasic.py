# Assign a list to an variable named my_list
my_list = [1,2,3]

my_list = ['A string',23,100.232,'o']

len(my_list) #4

my_list = ['one','two','three',4,5]

# Grab element at index 0
my_list[0] # one

# Grab index 1 and everything past it
my_list[1:] # ['two', 'three', 4, 5]

# Grab everything UP TO index 3
my_list[:3] # ['one', 'two', 'three']

my_list + ['new item'] #['one', 'two', 'three', 4, 5, 'new item']

"""
Note: This doesn't actually change the original list!
"""

my_list #['one', 'two', 'three', 4, 5]

# Reassign
my_list = my_list + ['add new item permanently']

# Make the list double
my_list * 2

"""
['one',
 'two',
 'three',
 4,
 5,
 'add new item permanently',
 'one',
 'two',
 'three',
 4,
 5,
 'add new item permanently']
"""

#Basic List Methods
# Create a new list
list1 = [1,2,3]

# Append
list1.append('append me!')

# Show
list1

# Pop off the 0 indexed item
list1.pop(0) # [2, 3, 'append me!']

# Assign the popped element, remember default popped index is -1
popped_item = list1.pop()

# We can use the sort method and the reverse methods to also effect your lists:
new_list = ['a','e','x','b','c']

# Use reverse to reverse order (this is permanent!)
new_list.reverse() # ['c', 'b', 'x', 'e', 'a']

# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort() #['a', 'b', 'c', 'e', 'x']

#Nesting Lists

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
"""
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
# Grab first item in matrix object
matrix[0] # [1, 2, 3]

# Grab first item of the first item in the matrix object
matrix[0][0] #1

#List Comprehensions
# Build a list comprehension by deconstructing a for loop within a []

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
first_col = [row[0] for row in matrix] # [1, 4, 7]

