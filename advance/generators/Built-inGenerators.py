# range()
r = range(1, 10, 2)  # Generates numbers from 1 to 9 with a step of 2
print(list(r))  # Output: [1, 3, 5, 7, 9]

# Iterating over range without converting to list
for num in range(3):
    print(num)
# Output:
# 0
# 1
# 2

#enumerate()
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names, start=1):
    print(index, name)

# Output:
# 1 Alice
# 2 Bob
# 3 Charlie


# zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(names, ages)  # Creates a generator

print(list(zipped))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


#iter()
lst = [10, 20, 30]
it = iter(lst)  # Creates an iterator

print(next(it))  # Output: 10
print(next(it))  # Output: 20
print(next(it))  # Output: 30
# print(next(it))  # Raises StopIteration

#map()
nums = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, nums)

print(list(squared))  # Output: [1, 4, 9, 16, 25]


#filter()
nums = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, nums)

print(list(evens))  # Output: [2, 4]


#reversed()
nums = [1, 2, 3, 4]
rev = reversed(nums)

print(list(rev))  # Output: [4, 3, 2, 1]

#open()
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Reads line-by-line lazily
