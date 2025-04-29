def stringOperations(teststring):
    print("test string %s" %(teststring))
    print("O position : " + teststring[0])
    print("O position : " + teststring[-1])

def stringOperationswithmultiple(teststring):

    print("O position : " + teststring*3)

def stringOperationswithtab(teststring):
    print("test hello\t\tworld")

def stringOperationsIndexes(teststring):
    print("0th postion " + teststring[0]) # a
    print("7th postion " + teststring[7]) # h
    print("-1st postion " + teststring[-1]) # h

    print("2: postion " + teststring[2:]) # cdefgh
    print(":2 postion " + teststring[:2])  # ab
    print("2:6 postion " + teststring[2:6])  # cdef
    print("2:-3 postion " + teststring[2:-3])  # cde

    print(":-3 postion " + teststring[:-3])  # abcde
    print(":-2 postion " + teststring[:-2])  # abcdef

    print(":: postion " + teststring[::])  # abcdefgh
    print(":: postion reverse " + teststring[::-1])  # hgfedcba
    print("::2 postion " + teststring[::2])  # aceg
    print("2:7:2 postion " + teststring[2:7:2])  # ceg

def specialOperator():
    num = '100'
    print(num.isdigit()) # True


if __name__=='__main__':
    #stringOperations('hello')
    #stringOperationswithtab('hello')

    #stringOperationsIndexes("abcdefgh")
    #stringOperationswithmultiple('z')
    specialOperator()

"""

hello
01234

abcdefgh
01234567

ab        cd           ef                    gh
0-7      -6-5          -4-3                  -2-1

"""