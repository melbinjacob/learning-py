price = 100
items = int(input("How much products did you buy ? "))

total = price*items

if total > 1000:
        print("Your total is " + str(total))
        print("Your total with 10% discount is " + str((total - (total*10)/100)))
else :
        print("Your total is " + str(total))
