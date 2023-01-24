def read_file(fname):
    with open("test.txt","r") as f:
        li = f.readlines()
        print(li)
read_file("test.txt")