#Return statements in python functions

def cube(num):
        print("This will get printed")
        return num*num*num
        Print("This will not print onto the terminal because the function exited after the return stement")
value = cube(100)
print(value)