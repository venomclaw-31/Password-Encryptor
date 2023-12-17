from cryptography.fernet import Fernet

# Uncomment the following function to generate the key only once
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

master_pwd = input("What is the master password? : ")

# Combine the bytes key with the master password bytes
key = load_key() + master_pwd.encode()

# Use the combined key to create the Fernet object
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_password = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_password)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    # Encrypt the password and decode it before writing to the file
    encrypted_password = fer.encrypt(pwd.encode()).decode()
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_password + "\n")

while True:
    mode = input("Would you like to add a new pass or view existing ones (view/add)? Press Q to quit: ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue
