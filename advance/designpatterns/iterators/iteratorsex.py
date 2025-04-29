#Built-in Iterables
#Most Python collections are iterable by default.

my_list = [1, 2, 3, 4]
iterator = iter(my_list)  # Create an iterator from the list

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
# Continue until the StopIteration exception is raised.

#Custom Iterators
#You can create a custom iterator by defining a class with __iter__() and __next__() methods.

class MyNumbers:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Using the custom iterator
numbers = MyNumbers(5)
for num in numbers:
    print(num)  # Output: 1, 2, 3, 4, 5


#Infinite Iterator
#You can use custom iterators to create infinite sequences.

class InfiniteNumbers:
    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        self.number += 1
        return self.number

infinite = InfiniteNumbers()
iterator = iter(infinite)

for _ in range(5):  # Print first 5 numbers
    print(next(iterator))
