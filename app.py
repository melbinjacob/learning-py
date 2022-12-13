name1 = input("What is your name? ")
person1 = int(input( name1 + " what's your age : "))

name2 = input("What is your name ? ")
person2 = int(input( name2 + " what's your age : "))

name3 = input("What is your name ? ")
person3 = int(input( name3 + " what's your age : "))

if person1 > person2 and person1 > person3:
        print(name1 + " is the oldest")
elif person1 == person2 and person2 == person3:
        print("All of you have the same age")
elif person2 > person1 and person2 > person3:
        print(name2 + " is the oldest")
else :
        print(name3 + " is the oldest")