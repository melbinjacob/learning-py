user_name = [
    "Mel",
    "Jaz",
    "Dev"
]

password = [
    "pass1",
    "pass1",
    "pass3"
]

password_input = ""

user_name_input = input("Enter your username: ")
if user_name_input in user_name:
    password_input = input("Enter your password: ")
    posu = user_name.index(user_name_input)
    posp = password.index(password_input)
else:
    print("User not found!")
if posu == posp:
    
    print("Welcome " + user_name_input)
else:
    print("Wrong password")