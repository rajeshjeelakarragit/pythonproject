def square(num):
    return num **2

my_nums = [1,2,3,4,5]

for item in map(square , my_nums):
    print(item)

"""

1
4
9
16
25

"""

print(map(square , my_nums)) # <map object at 0x0000027A7EBFCB80>
print(list(map(square , my_nums))) # [1, 4, 9, 16, 25]


def check_even(num):
    return num %2 == 0

print(filter(check_even , my_nums)) # <filter object at 0x0000012A37E1E2C0>
print(list(filter(check_even , my_nums))) # [2, 4]



def square(num):
    result = num **2
    return result


def squareshort(num): return num **2

squarelambda = lambda num:  num **2

print(squarelambda(3))
print(list(map(lambda num:  num **2 , my_nums)))