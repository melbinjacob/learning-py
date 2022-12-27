num = int(input("Enter a number: "))
if num % 5 == 0 and num % 3 == 0 :
    print("TF")
elif num % 3 == 0:
    print("T")
elif num % 5 == 0:
    print("F")
else:
    print("Not T, nor F")