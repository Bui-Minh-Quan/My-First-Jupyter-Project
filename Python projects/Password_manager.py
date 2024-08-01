from cryptography.fernet import Fernet

def load_key():
    file = open("Python projects\key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("Python projects\password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print("Name:", name, "|Password:", fer.decrypt(password).decode())

def add():
    name = input("User name: ")
    password = input("User password: ")
    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode())

while True:
    mode = input("Would you like to add or view existing accounts(add/view), press q to quit: ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()
    else:
        print("Invalid command")
        continue


