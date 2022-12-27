while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0 :
        print("Even")
    else:
        print("Odd")
    k = input("Do you want to continue (Press Y): \n Else press any key:")
    if k.lower() == "y":
        continue
    else:
        break