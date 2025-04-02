def forloopwithcompile():
    for char in "Narayana":
        print(char , end='')

def forloopwithparameter(name):
    for char in name:
        print(char , end='')

def forloopwithstring():
    zen = '''
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    '''

    for char in zen:
        if char not in 'aeiou':
           print(char, end='')

forloopwithstring()