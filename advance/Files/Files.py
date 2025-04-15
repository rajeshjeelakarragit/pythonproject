# Create a new file
file = open("example.txt", "w")
file.close()
print("File created successfully.")

# Create a file and write content
with open("example_with_content.txt", "w") as file:
    file.write("Hello, this is a new file with some content!")
print("File with content created successfully.")

try:
    with open("unique_file.txt", "x") as file:
        file.write("This file is created only if it does not already exist.")
    print("File created successfully.")
except FileExistsError:
    print("File already exists.")

open("C:/Users/YourName/Documents/newfile.txt", "w")

with open("example.txt", "a") as file:
    file.write("\nAdditional content added.")

"""
myfile = open('whoops.txt')

myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")

# We can now read the file
myfile.read()

# Seek to the start of file (index 0)
myfile.seek(0)


# Readlines returns a list of the lines in the file
myfile.seek(0)
myfile.readlines()

myfile.close()

#Writing to a File

# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt','w+')

# Write to the file
my_file.write('This is a new line')

# Read the file
my_file.seek(0)
my_file.read()

my_file.close()  # always do this when you're done with a file

#Appending to a File

my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')

my_file.seek(0)
print(my_file.read())

my_file.close()

for line in open('test.txt'):
    print(line)

 """

################################################################################

"""
# Opening a file in read mode
file = open("example.txt", "r")

# Opening a file in write mode
file = open("example.txt", "w")

# Opening a file in append mode
file = open("example.txt", "a")

# Opening a file in binary read mode
file = open("example.txt", "rb")


# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()

 """

""" 
read() − Reads the entire file.

readline() − Reads one line at a time.

readlines − Reads all lines into a list.

"""

"""
with open("example.txt", "r") as file:
   content = file.read()
   print(content)

"""


"""
with open("example.txt", "r") as file:
   line = file.readline()
   while line:
      print(line, end='')
      line = file.readline()

"""

"""
with open("example.txt", "r") as file:
   lines = file.readlines()
   for line in lines:
      print(line, end='')

"""

"""
with open("foo.txt", "w") as file:
   file.write("Hello, World!")
   print ("Content added Successfully!!")

"""


"""
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
   file.writelines(lines)
   print ("Content added Successfully!!")

"""

"""
try:
   file = open("example.txt", "w")
   file.write("This is an example with exception handling.")
finally:
   file.close()
   print ("File closed successfully!!")
"""