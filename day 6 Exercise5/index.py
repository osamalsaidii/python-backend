import re

def is_strong_password(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r"[A-Z]", pwd):
        return False
    if not re.search(r"[a-z]", pwd):
        return False
    if not re.search(r"\d", pwd):
        return False
    if not re.search(r"[!@#$%^&*]", pwd):
        return False
    return True

try:
    with open("passwords.txt", "r") as infile:
        passwords = [line.strip() for line in infile]

    with open("strong_passwords.txt", "w") as outfile:
        for pwd in passwords:
            if is_strong_password(pwd):
                outfile.write(pwd + "\n")
            else:
                print(f"Password '{pwd}' is weak and was skipped.")

except FileNotFoundError:
    print("Error: 'passwords.txt' not found.")
except IOError:
    print("Error: Could not read or write file.")
