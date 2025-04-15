def create_cubes(n):
    result = []
    for x in range(n): #range(n) = [0,1,2,3,4]
        result.append(x**3)
    return result

#print(create_cubes(5))

def create_cubes_yield(n):
    #result = []
    for x in range(n):
       #result.append(x**3)
       yield x**3
    #return result

#print(create_cubes_yield(5)) #<generator object create_cubes_yield at 0x000001E68FCA351

#for cube in create_cubes_yield(5):
         #print(cube)

def gen_fibn(n):

    a=1
    b=1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b , a+b
    return output

#print(gen_fibn(5))


def gen_fibn_yield(n):

    a=1
    b=1
    #output = []
    for i in range(n):
        #output.append(a)
        yield a
        a,b = b , a+b
    #return output

#for number in gen_fibn_yield(5):
     #print(number)

def simple_gen():
    for x in range(3):
        yield x

#for number in simple_gen():
    #print(number)

g = simple_gen()
print(next(g))
print(next(g))