#Functions
def display():
    print("this is display function")

def displaywithArguments(name):
    print("Hello this is function with arguments %s " %(name))

def displaywithMoreArguments(row1 , row2 , ro3):
    print(f"Argument List - {row1}  {row2} {row3}")

# Arbitrary Positional Arguments)
# (Arbitrary Keyword Arguments)
def displaywithRexArguments(*row , **kwargs):
    print(f"Reg Argument List - {row[0]}  {row[1]} {row[2]} {kwargs['rowList']}")

def print_keyword_args(**kwargs):
    print(f"Keyword arguments: {kwargs}")

"""
# Output: Keyword arguments: {'a': 1, 'b': 2, 'c': 3}
"""

def print_positional(*row):
    print(f"Positional arguments: {row}")
"""
# Output: Positional arguments: (1, 2, 3, 4)
"""

def process_data(*row, **kwargs):
    print(f"Positional arguments: {row}")
    print(f"Keyword arguments: {kwargs}")




def example_function(a, b, *row, c, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"Additional positional args: {row}")
    print(f"Keyword-only argument c: {c}")
    print(f"Additional keyword args: {kwargs}")

"""
# Output:
# a: 1, b: 2
# Additional positional args: (3, 4)
# Keyword-only argument c: 5
# Additional keyword args: {'d': 6, 'e': 7}

"""


if __name__ == '__main__':
    #display()
    #displaywithArguments("python")

    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,8,9]

    #displaywithMoreArguments(row1 , row2 , row3)

    #displaywithRexArguments(row1, row2, row3 , rowList=[10,20,30])

    #print_keyword_args(a=1, b=2, c=3)

    #process_data(1, 2, 3, name="Alice", age=25)

    #print_positional(1, 2, 3, 4)

    #example_function(1, 2, 3, 4, c=5, d=6, e=7)

