mark = float(input("Enter your Marks : "))

if mark < 0 :
        print("Invalid input")
elif mark < 25:
        print("Your grade is : F")
elif mark <= 45:
        print("Your grade is : D")
elif mark <= 50:
        print("Your grade is : D")
elif mark <= 60:
        print("Your grade is : C")
elif mark <= 80:
        print("Your grade is : B")
else :
        print("Your grade is : A")