#Generator Function (Using yield)
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(5)  # Creating a generator object

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
print(next(gen))  # Output: 5

#Generator Expression
gen_exp = (x * x for x in range(5))

print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1
print(next(gen_exp))  # Output: 4

# Iterating Over a Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)

# Output:
# 0
# 1
# 1
# 2
# 3

#Sending Values to a Generator (send())
def echo():
    while True:
        received = yield
        print("Received:", received)

gen = echo()
next(gen)  # Start the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("Python")  # Output: Received: Python


#5. Generator Methods

#Converting a Generator to a List
gen = (x * x for x in range(5))
print(list(gen))  # Output: [0, 1, 4, 9, 16]


#Practical Use Cases
def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

for line in read_large_file("large_file.txt"):
    print(line)



