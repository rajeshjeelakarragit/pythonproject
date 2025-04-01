mystring="hello"
mylist = []
for letter in mystring:
    mylist.append(letter)

#print("After appending : %s" %mylist ) #['h', 'e', 'l', 'l', 'o']

mylist = [letter for letter in mystring] #['h', 'e', 'l', 'l', 'o']
#print("append : %s" %mylist)

mylist = [letter for letter in "word"]
#print(mylist)

mylist = [num for num in range(0,10)]
#print(mylist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mylist = [num*2 for num in range(0,10)]
#print(mylist) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

mylist = [num for num in range(0,10) if num%2==0]
#print(mylist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #[0, 2, 4, 6, 8]

mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

#print(mylist) # [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist)


# Grab every letter in string
lst = [x for x in 'word'] #['w', 'o', 'r', 'd']

# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0] # [0, 2, 4, 6, 8, 10]

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ]

fahrenheit #[32.0, 50.0, 68.18, 94.1]


lst = [ x**2 for x in [x**2 for x in range(11)]]
lst #[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]


