class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Attempted to withdraw {amount}, but only {balance} is available.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
except InsufficientFundsError as e:
    print("Bank error:", e)
