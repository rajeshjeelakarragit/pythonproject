def gen_fun12():
    numlist = []
    for num in range(10):
        numlist.append(num)
    return numlist


def gen_fun():
    for num in range(10):
        yield num


print(gen_fun())

gen = gen_fun()

# Generate values using next()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
print(next(gen))  # Output: 5

print(next(gen))  # Output: 6
print(next(gen))  # Output: 7
print(next(gen))  # Output: 8

print(next(gen))  # Output: 9


def infinite_sequence():
    num = 3
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for _ in range(5):  # Print first 5 numbers
    print(next(gen))