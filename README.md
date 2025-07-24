# Password Validator

A simple Python script to interactively validate passwords based on specific security requirements.

---

## Features

- Enforces a minimum length of 8 characters
- Requires at least one letter (A-Z or a-z)
- Requires at least one digit (0-9)
- Requires at least one special character from: `# @ % $`
- Password must end with a digit
- Rejects passwords with invalid characters

---

## How It Works

The script uses regular expressions (`re` module) to check that the password:

- Meets all above criteria
- Contains only allowed characters (letters, digits, and specified special characters)

If a password fails any rule, it prompts the user with a specific message and asks for a new input.

---

## Usage

1. Make sure you have Python installed (Python 3 recommended).

2. Run the script:

```bash
python script.py
