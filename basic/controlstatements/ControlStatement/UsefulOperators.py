range(0,11) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Notice how 11 is not included, up to but not including 11, just like slice notation!
list(range(0,11))

# Third parameter is step size!
# step size just means how big of a jump/leap/step you
# take from the starting number to get to the next number.

list(range(0,11,2)) #[0, 2, 4, 6, 8, 10]

#enumerate

index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

"""
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e

"""

# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

"""
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e

"""

#zip

list(enumerate('abcde')) #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

# This one is also a generator! We will explain this later, but for now let's transform it to a list
zip(mylist1,mylist2) #<zip at 0x1d205086f08>

list(zip(mylist1,mylist2)) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))

"""
For this tuple, first item was 1 and second item was a
For this tuple, first item was 2 and second item was b
For this tuple, first item was 3 and second item was c
For this tuple, first item was 4 and second item was d
For this tuple, first item was 5 and second item was e
"""

#in operator
'x' in ['x','y','z'] #True
'x' in [1,2,3] # False

#not in
'x' not in ['x','y','z'] #False
'x' not in [1,2,3] # True

#min and max
mylist = [10,20,30,40,100]
min(mylist)
max(mylist)

#random
from random import shuffle

mylist = [10,20,30,40,100]

# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist) #[40, 10, 100, 30, 20]

from random import randint
# Return random integer in range [a, b], including both end points.
randint(0,100) #25

# Return random integer in range [a, b], including both end points.
randint(0,100) #91

#input
input('Enter Something into this box: ')


