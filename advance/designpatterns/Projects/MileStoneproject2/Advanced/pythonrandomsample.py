import random

print(random.randint(0,100))
random.seed(42)
random.seed(101)
random.randint(0,100)

mylist = list(range(1,20)) # [1....19]
random.choice(mylist) # 16

# Sample with Replacement
#random.choice(population=mylist , k=10)


# Sample without Replacement
#random.sample(population=mylist , k=10)

random.shuffle(mylist)

random.uniform(a=1 , b=100)

random.gauss(mu=0 , sigma=1)