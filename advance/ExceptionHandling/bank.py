class InvalidUsernameError(Exception):
    pass

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}. Available balance: {balance}")

def validate_username(username):
    if len(username) < 5:
        raise InvalidUsernameError("Username must be at least 5 characters.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# ----- Main block -----
try:
    username = input("Enter your username: ")
    validate_username(username)

    balance = 1000
    amount = float(input("Enter amount to withdraw: "))

    new_balance = withdraw(balance, amount)
    print(f"Withdrawal successful. New balance: {new_balance}")

except InvalidUsernameError as e:
    print("Username error:", e)

except InsufficientFundsError as e:
    print("Transaction error:", e)

except ValueError:
    print("Invalid input: please enter numbers only.")

except Exception as e:
    print("Unexpected error occurred:", e)

finally:
    print("Thank you for using our service.")
