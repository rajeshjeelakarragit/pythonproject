def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

#Generator Expression
gen_expr = (x * x for x in range(5))  # Creates a generator for squares

for value in gen_expr:
    print(value)



def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for _ in range(5):  # Print first 5 numbers
    print(next(gen))

#Fibonacci Sequence

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
for num in fibonacci(10):
    print(num)

"""
Generator Methods
next(generator): Retrieve the next value from a generator.
.send(value): Send a value to the generator (used in coroutines).
.close(): Stop the generator.

"""


def echo():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo()
next(gen)  # Start the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World