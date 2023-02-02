class person:
    def __init__(self) :
        print("Hello")
class stud(person):
    def __init__(self):
        super().__init__()

p = stud()
stud()