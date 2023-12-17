# Password Manager

This is a simple password manager that uses the `cryptography` library to encrypt and decrypt passwords. It prompts the user for a master password, combines it with a stored key, and uses the resulting key to encrypt and decrypt passwords.

## Setup

1. **Generate Key:**
   Uncomment and run the `write_key` function once to generate the encryption key. It will create a file named `key.key`.

    ```bash
    python3 your_script_name.py
    ```

2. **Run the Password Manager:**
   Run your password manager script.

    ```bash
    python3 your_script_name.py
    ```

## Features

- **View Passwords:**
  - Lists all stored usernames and decrypted passwords.

- **Add Password:**
  - Allows you to add a new account name and password, encrypting the password for storage.

## Usage

1. Run the script and provide the master password when prompted.

2. Choose between viewing existing passwords or adding a new one.

3. Follow the prompts to view or add passwords.

## Important Note

- Make sure to remember your master password. It is crucial for decrypting passwords.

## Security

- The master password is combined with a stored key to enhance security.

## Dependencies

- [cryptography](https://cryptography.io): A library for secure communication.

## License

This project is licensed under the [MIT License](LICENSE).
