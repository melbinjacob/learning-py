classes_held = int(input("How many classes was held : "))
classes_attented = int(input("How many classes did you attent : "))


persentage = (classes_attented/classes_held) * 100

if persentage < 75 :
        print("You only have " + str(persentage) + "% Attentance You are not eligible for the exam")
else:
        print("You have " + persentage + "% Attentance you are eligible for the exam")