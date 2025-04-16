try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("Caught an exception:", e)


try:
    num = int(input("Enter a number: "))  # Could raise ValueError
    result = 10 / num                     # Could raise ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print("Caught an exception:", e)
else:
    print("Result:", result)
finally:
    print("Done.")



class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    result = 10 / num
except (ValueError, ZeroDivisionError, NegativeNumberError) as e:
    print("Handled error:", e)
else:
    print("Result is:", result)
finally:
    print("Execution completed.")
