numbers = [10,11,12,13]

for num in numbers:
    print(num)

names = ["Jacob", "Joe", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")