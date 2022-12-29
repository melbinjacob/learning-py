num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter anoter number again: "))

if num1>num2>num3:
    print("First number " + str(num1) + " is the biggest number.")
elif num2>num1>num3:
    print("Second number " + str(num2) + " is the biggest number.")
elif num3>num2>num1:
    print("Third number " + str(num3) + " is the biggest number.")