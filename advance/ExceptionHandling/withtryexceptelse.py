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