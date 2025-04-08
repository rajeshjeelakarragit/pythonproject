# Program to add two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum is:", sum)
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))