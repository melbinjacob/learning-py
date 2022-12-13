salary = int(input("Enter your salary : "))

years = int(input("How much years of  work expirence do you have in this company? : "))

if years > 5:
        print("Your salary with bonus is : " + str((salary+(salary*5)/100)))
else:
        print("Your work expireience is not greater than 5 years. So you have NO BONUS!")