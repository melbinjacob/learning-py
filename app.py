cont = ""
def oddEven(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    global cont 
    cont = input("Do you want to check another number?(Y) or press any other key to exit!: ")


oddEven(int(input("Enter a number: ")))

while cont.upper() == "Y":
    oddEven(int(input("Enter a number: ")))
