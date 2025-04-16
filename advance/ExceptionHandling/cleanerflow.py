try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
else:
    print("Result is:", result)
finally:
    print("This will run no matter what.")


try:
    # some risky operation
    a = 10 / int("abc")
except Exception as e:
    print("Something went wrong:", e)