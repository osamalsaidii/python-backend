class InvalidLengthError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass

def validate_username(username):
    if not (5 <= len(username) <= 15):
        raise InvalidLengthError("Username must be between 5 and 15 characters.")
    if not username.isalnum():
        raise InvalidCharacterError("Username must be alphanumeric.")

try:
    username = input("Enter a username: ").strip()
    validate_username(username)
    
    with open("users.txt", "a") as file:
        file.write(username + "\n")
    print("Username registered successfully.")

except InvalidLengthError as e:
    print("Length Error:", e)
except InvalidCharacterError as e:
    print("Character Error:", e)
except IOError:
    print("Error: Could not write to 'users.txt'.")
finally:
    print("Registration attempt complete.")
