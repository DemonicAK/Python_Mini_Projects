import string
import secrets
import random


def generate_password(length: int) -> str:
    """
    Generate a strong random password.

    Args:
    length (int): Desired length of the password. Minimum length is 12.

    Returns:
    str: A randomly generated password.

    The password will contain at least one lowercase letter, one uppercase letter,
    one digit, and one special character.
    """
    LOWERCASE_CHARS = string.ascii_lowercase
    UPPERCASE_CHARS = string.ascii_uppercase
    DIGITS = string.digits
    SPECIAL_CHARS = string.punctuation

    MIN_LENGTH = 12

    # Ensure the password length is at least the minimum
    password_length = max(length, MIN_LENGTH)

    # Create a pool of all possible characters
    all_chars = LOWERCASE_CHARS + UPPERCASE_CHARS + DIGITS + SPECIAL_CHARS

    # Ensure we have one of each required character type
    required_chars = [
        secrets.choice(LOWERCASE_CHARS),
        secrets.choice(UPPERCASE_CHARS),
        secrets.choice(DIGITS),
        secrets.choice(SPECIAL_CHARS)
    ]

    # Generate the remaining characters
    remaining_length = password_length - len(required_chars)
    random_chars = [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Combine all characters
    all_password_chars = required_chars + random_chars

    # Shuffle the characters to randomize their position
    random.shuffle(all_password_chars)

    # Join the characters into a string
    password = ''.join(all_password_chars)

    return password


def main():
    try:
        desired_length = int(input('Enter desired password length: '))
        password = generate_password(desired_length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")


if __name__ == "__main__":
    main()
