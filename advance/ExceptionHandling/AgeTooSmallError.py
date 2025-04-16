class AgeTooSmallError(Exception):
    def __init__(self, age, message="Age is too small!"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise AgeTooSmallError(age)
    print("Age is acceptable.")

try:
    check_age(15)
except AgeTooSmallError as e:
    print(f"Error: {e.message} (Given age: {e.age})")
