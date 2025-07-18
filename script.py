import re

# Explanation:
# - (?=.*[A-Za-z]) → at least one letter
# - (?=.*\d)       → at least one digit
# - (?=.*[$%#@])   → at least one special character
# - .{8,}          → minimum 8 characters
# - \d$            → ends with a digit
pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$%#@])[A-Za-z\d$%#@]{8,}\d$')

print("Password Requirements:")
print("- At least 8 characters")
print("- Must include letters")
print("- Must include numbers")
print("- Must include one of the following: # @ % $")
print("- Must end with a number\n")

while True:
    password = input("Create a password: ")

    if not len(password) >= 8:
        print("❌ Password must be at least 8 characters.")
        continue

    if not re.search(r'[A-Za-z]', password):
        print("❌ Password must contain at least one letter.")
        continue

    if not re.search(r'\d', password):
        print("❌ Password must contain at least one digit.")
        continue

    if not re.search(r'[$%#@]', password):
        print("❌ Password must include at least one special character (# @ % $).")
        continue

    if not password[-1].isdigit():
        print("❌ Password must end with a digit.")
        continue

    if not pattern.fullmatch(password):
        print("❌ Password contains invalid characters.")
        continue

    print("✅ Password is valid!")
    break
