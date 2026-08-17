import random
import string


def generate_password():
    try:
        length = int(input("Enter the desired password length: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return None

    include_uppercase = input(
        "Include uppercase letters? (yes/no): "
    ).strip().lower()

    include_special = input(
        "Include special characters? (yes/no): "
    ).strip().lower()

    include_digits = input(
        "Include digits? (yes/no): "
    ).strip().lower()

    if length < 4:
        print("Password length must be at least 4 characters.")
        return None

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""

    all_characters = lower + uppercase + special + digits

    required_characters = []

    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))

    if include_special == "yes":
        required_characters.append(random.choice(special))

    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    # Make sure the requested length is enough
    if length < len(required_characters):
        print("Password length is too short for the selected options.")
        return None

    remaining_length = length - len(required_characters)

    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    return "".join(password)


def check_password_strength(password):
    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    # Character types
    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    # Strength
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 5:
        return "Strong"
    else:
        return "Very Strong"


# Generate password
password = generate_password()

# Only check strength if password was successfully generated
if password:
    print("\nGenerated Password:", password)

    strength = check_password_strength(password)

    print("Password Strength:", strength)
