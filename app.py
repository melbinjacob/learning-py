secret_word = "melbin"

guess = ""

tries = 0
left = 4

while tries <= 3 and guess != secret_word:
        guess = input("I am you enter who am I : ")
        tries = tries + 1
        no = left - tries
        
        if guess == secret_word:
                print("You won!")
        else: 
                print("You have " + str(no) + " tries left!")
                if no == 0 :
                        print("You have no tries left you have lost the game")
