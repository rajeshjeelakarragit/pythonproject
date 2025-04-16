class InvalidUsernameError(Exception):
    def __init__(self, username):
        super().__init__(f"'{username}' is not a valid username. Must be at least 5 characters.")

def check_username(username):
    if len(username) < 5:
        raise InvalidUsernameError(username)
    print("Username is valid.")

try:
    check_username("abc")
except InvalidUsernameError as e:
    print("Validation failed:", e)
