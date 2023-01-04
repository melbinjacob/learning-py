import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "sissors"]

while True:
    user_input = input("Type Rock/Paper/Sissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Enter a valid input")
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if computer_pick == user_input:
        print("You also picked", user_input , "Nobody won.")
    elif user_input == "rock" and computer_pick == "sissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "sissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1
    
print("You got", user_wins , "Points.")
print("The computer got", computer_wins , "Points.")
print("Goodbye!")