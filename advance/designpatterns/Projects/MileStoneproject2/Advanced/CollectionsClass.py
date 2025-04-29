from collections import Counter , defaultdict , namedtuple
my_list=[1,1,2,2]

count_list=Counter(my_list)
print(count_list) # Counter({1: 2, 2: 2})

d = defaultdict(lambda:0)
d['correct'] = 100
print(d) # (<function <lambda> at 0x000001C4704B5C60>, {'correct': 100})
print(d['correct'])

my_tuple = (10,20,30)
print(my_tuple[0])

Dog12 = namedtuple('Dog' , ['age' , 'breed' , 'name'])
print(type(Dog12)) # <class 'type'>

sammy = Dog12(age=5 , breed='Husky' , name='Sam')
print(type(sammy)) # <class '__main__.Dog'>

print(sammy.age) #Dog(age=5, breed='Husky', name='Sam')