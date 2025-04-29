def dataTypeOperations():
    print(7/4) #1.75
    print(7 // 4)  # 1
    print(7%4) #3
    print(2**3) #8
    print(2>3) # False
    print(2 < 3)  # True
    print(1<2<3) # True
    print(1<2>3) # False
    print(1 < 2 and 2 > 3)  # False
    print(1==1)  # True
    print(not 1 == 1)  # False

def NoneOpearions():
    b=None
    if b is not None:
        print(b)
    else:
        print('b i not none')


if __name__=='__main__':
    NoneOpearions()