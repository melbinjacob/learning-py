from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user,",", "Password: ", passw)
def add():
    name = input("Account Name: ")
    pwd = input("Enter Your password: ")
    with open("passwords.txt","a") as f:
        f.write(name + "|" + pwd +"\n")

while True:
    mode = input("Would you like to view your existing password or add a new one (View/Add)? or press Q to quit: ").lower()
    if  mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add() 

    else:
        print("Invalid input")
        continue