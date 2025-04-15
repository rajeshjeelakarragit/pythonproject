def gen_squares(n):

    for number in range(n):
        yield number **2

#for x in gen_squares(10):
   #   print(x)
gen = iter( gen_squares(10))
#print(next(gen))
#print(next(gen))


import random

def rand_num(low , high , n):
   for i in range(n):
       yield random.randint(low , high)

for num in rand_num(1 , 10 , 12):
    print(num)


my_list = [1,2,3,4,5]
gen_comp = (item for item in my_list if item > 3)

for item in gen_comp:
    print(item)
