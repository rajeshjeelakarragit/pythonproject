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


for cube in create_cubes_yield(5):
         print(cube)