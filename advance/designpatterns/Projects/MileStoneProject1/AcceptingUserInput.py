def takeInputFromUser():
    result = input("Please enter a value ")
    print(type(result))
    """
    str
    """

def takeInputFromUserThenConvertToInteger():
    result = input("Please enter a value ")
    result_int = int(result)
    print(result_int)
    """
    int
    """


if __name__ =='__main__':
    takeInputFromUserThenConvertToInteger()
else:
    print("this is end program")