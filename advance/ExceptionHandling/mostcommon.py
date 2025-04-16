try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("You entered an invalid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
