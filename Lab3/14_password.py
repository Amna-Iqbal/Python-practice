print("Password Requirements:")
print("At least 1 letter between [a-z] and 1 letter between [A-Z]")
print("At least 1 number between [0-9]")
print("At least 1 character from [$#@]")
print("Minimum length: 6")
print("Maximum length: 16")

password = input("Enter a password: ")
valid_password = True

if len(password) < 6 or len(password) > 16:
    print("Password length must be between 6 and 16 characters.")
    valid_password = False

if not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter (a-z).")
    valid_password = False

if not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter (A-Z).")
    valid_password = False

if not any(char.isdigit() for char in password):
    print("Password must contain at least one digit (0-9).")
    valid_password = False

if not any(char in ['$', '#', '@'] for char in password):
    print("Password must contain at least one of the following characters: $, #, @.")
    valid_password = False

if valid_password:
    print("Password is valid.")
else:
    print("Password does not meet the requirements.")

