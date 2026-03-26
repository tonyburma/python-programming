# custom exception class
class InvalidPasswordError(Exception):
    """Exception raised for invalid password."""

    def __init__(self, message="Password must be at least 8 characters long."):
        self.message = message
        super().__init__(self.message)

def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError()
    else:
        print("Password is valid.")

# Example usage
try:
    user_password = input("Enter your password: ")
    validate_password(user_password)
except InvalidPasswordError as e:
    print(f"Invalid password: {e}")

