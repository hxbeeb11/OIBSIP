import random
import string

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Error: At least one character type (letters, numbers, symbols) must be selected.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Set your preferences here
    password_length = 16
    include_letters = True
    include_numbers = True
    include_symbols = True
    
    password = generate_password(password_length, include_letters, include_numbers, include_symbols)
    
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
