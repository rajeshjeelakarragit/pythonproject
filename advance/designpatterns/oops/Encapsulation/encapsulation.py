class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")

# Create an instance
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)

# Accessing private attribute directly (will fail)
# print(account.__balance)  # Uncomment to see the error
