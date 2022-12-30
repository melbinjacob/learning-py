users ={
    "Arun" : "Pass1",
    "Brun" : "Pass2",
    "Crun" : "Pass3",
    "Drun" : "Pass4",
    "Erun" : "Pass5",
}

user_name = input("Enter your username: ")
if user_name in users:
    password = input("Enter your password: ")
    if users[user_name] == password:
        print("Welcome " + user_name)
    else:
        print("Wrong password!")
else:
    print("User not found!")