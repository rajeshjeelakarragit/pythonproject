def withtryexceptfinally():

   while True:
        try:
            inter = int(input("Enter the integer : "))
            print(inter ** 2)
        except ZeroDivisionError:
            print("division by zero")
        except TypeError:
            print("TypeError")
            continue
        except ValueError:
            print("ValueError")
            continue
        else:
            print("else block")
            break
        finally:
            print("finally block")

withtryexceptfinally()

"""
Enter the integer : rajr
ValueError
finally block
Enter the integer : 233
54289
else block
finally block


"""

try:
    num = int(input("Enter a number: "))  # Could raise ValueError
    result = 10 / num                     # Could raise ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print("Caught an exception:", e)
else:
    print("Result:", result)
finally:
    print("Done.")