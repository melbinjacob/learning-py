print("Welcome to my Game!")
playing = input("Do you want to play the game? ")
if playing.upper() != "YES":
    quit()
print("Okay! let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.upper() == "GRAPHICS PROCESSING UNIT":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.upper() == "RANDOM ACESS MEMORY":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.upper() == "POWER SUPPLY":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your score is " + str(score))
print("Your percentage is " + str((score/4)*100)+"%")