secret_word = "melbin"
guess = ""

no_of_guess = 0
guess_limit = 3
lost = False

while secret_word != guess and not(lost):
        if no_of_guess < guess_limit:
                guess = input("I am you Enter Who am I: ")
                no_of_guess += 1
        else:
                lost = True
if lost:
        print("You have no guesses left and YOU LOST THE GAME!")
else:
        print("You won!")
