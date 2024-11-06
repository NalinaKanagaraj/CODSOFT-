import random
import string
length = int(input("Enter the desired length of the password: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'
characters  = string.ascii_lowercase
if include_uppercase:
    characters += string.ascii_uppercase
if include_digits:
    characters += string.digits
if include_special:
    characters += string.punctuation
if not characters:
    print("You must include at least one character type!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
