#This is program with output
import string
import secrets
import sys

def check_strength(password):
    """Calculates and returns a formatted strength string."""
    if len(password) < 6:
        return "Weak "
    elif len(password) < 10:
        return "Medium "
    else:
        return "Strong "

def generate_password():
    print("\n--- Hacker Password Generator ---")
    
    try:
        # Get Length
        length_input = input("Enter password length (default 12): ")
        length = int(length_input) if length_input.strip() else 12

        if length < 4:
            print("Error: Minimum length is 4.")
            return

        # Settings
        print("\nInclude character types? (y/n)")
        use_upper = input("Uppercase? (A-Z): ").lower() == 'y'
        use_lower = input("Lowercase? (a-z): ").lower() == 'y'
        use_digits = input("Digits? (0-9): ").lower() == 'y'
        use_symbols = input("Symbols? (!@#): ").lower() == 'y'

        characters = ""
        if use_upper: characters += string.ascii_uppercase
        if use_lower: characters += string.ascii_lowercase
        if use_digits: characters += string.digits
        if use_symbols: characters += string.punctuation

        if not characters:
            print("Error: Select at least one character type.")
            return

        # Generation using secrets for security
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        strength = check_strength(password)
        
        print("\n" + "="*30)
        print(f"PASSWORD: {password}")
        print(f"STRENGTH: {strength}")
        print("="*30)
        print("\n(Note: Copy manually from terminal)")

    except ValueError:
        print(" Error: Please enter a valid number for length.")

if __name__ == "__main__":
    while True:
        generate_password()
        if input("\nGenerate another? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break

Output:
---  Hacker Password Generator ---
Enter password length (default 12): 16

Include character types? (y/n)
Uppercase? (A-Z): y
Lowercase? (a-z): y
Digits? (0-9): y
Symbols? (!@#): y

==============================
PASSWORD: b7#R9[vQ!p2Lz*Xm
STRENGTH: Strong 
==============================

(Note: Copy manually from terminal)

Generate another? (y/n): n
Goodbye! 


