def tryexceptfinally():

    try:
        x = 5
        y = 0

        z = x / y
    except ZeroDivisionError:
        print("division by zero")
    finally:
        print("Everything fine")

tryexceptfinally()