def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)

    return result

print(create_cubes(5)) # [0, 1, 8, 27, 64]

for x in create_cubes(5):
    print(x)


def create_cubesyield(n):
    for x in range(n):
       yield x**3

for x in create_cubesyield(5):
    print(x)

"""
0
1
8
27
64
"""

def gen_fib(n):
    a=1
    b=1

    for i in range(n):
        yield a
        a,b= b, a+b

print(list(gen_fib(5))) # [1, 1, 2, 3, 5]


#Using a Generator Function:
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

#Using a Generator Expression:
gen = (x * x for x in range(5))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

#Streaming Data Processing:

def process_data(data_stream):
    for data in data_stream:
        yield data.upper()

gen = process_data(["hello", "world"])
for item in gen:
    print(item)

#Reading Large Files:
def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line

for line in read_large_file('large_file.txt'):
    print(line)

#Built-in Functions Supporting Generators
#sum(), list(), max(), min(), etc., work with generators

gen = (x * 2 for x in range(10))
print(sum(gen))  # Output: 90