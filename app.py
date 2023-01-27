class Animal:
    def __init__(myAnim, name, age):
        myAnim.name = name
        myAnim.age = age
    def animPrint(aName):
        print("Hey my animal is " + aName.name + " and he is " + aName.age)
nm = input("What is your animals name: ")  
ag = input("Your animals age: ")
a = Animal(nm,ag)
a.animPrint()