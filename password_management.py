"""
Password Manager

This script implements a simple password manager using the Fernet symmetric encryption
from the cryptography library. It allows users to add new passwords and view existing ones.
Passwords are stored in an encrypted format in a text file.

The Fernet library provides a secure way to encrypt and decrypt data. It uses a secret key
for symmetric encryption, ensuring that the data can only be accessed by those who have the key.

Dependencies:
- cryptography

Usage:
1. Ensure you have generated a key file named "key.key" before running this script.
2. Run the script and follow the prompts to add or view passwords.
"""

from cryptography.fernet import Fernet


def load_key():
    """
    Load the previously generated key from the key file.

    Returns:
    bytes: The encryption key.
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()


def view_passwords(fernet):
    """
    View all stored passwords.

    Args:
    fernet (Fernet): The Fernet instance for decryption.
    """
    try:
        with open('passwords.txt', 'r') as file:
            for line in file:
                data = line.rstrip()
                user, encrypted_pass = data.split("|")
                decrypted_pass = fernet.decrypt(
                    encrypted_pass.encode()).decode()
                print(f"Account: {user} | Password: {decrypted_pass}")
    except FileNotFoundError:
        print("No passwords stored yet.")
    except Exception as e:
        print(f"An error occurred while viewing passwords: {e}")


def add_password(fernet):
    """
    Add a new password to the storage.

    Args:
    fernet (Fernet): The Fernet instance for encryption.
    """
    account = input('Account Name: ')
    password = input("Password: ")

    try:
        with open('passwords.txt', 'a') as file:
            encrypted_pass = fernet.encrypt(password.encode()).decode()
            file.write(f"{account}|{encrypted_pass}\n")
        print("Password added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the password: {e}")


def main():
    key = load_key()
    fernet = Fernet(key)

    while True:
        mode = input(
            "Would you like to add a new password (add), view existing ones (view), or quit (q)? ").lower()

        if mode == "q":
            break
        elif mode == "view":
            view_passwords(fernet)
        elif mode == "add":
            add_password(fernet)
        else:
            print("Invalid mode. Please choose 'add', 'view', or 'q'.")


if __name__ == "__main__":
    main()
