li = []
with open("test.txt","r") as f:
    for x in f:
        li.append(x.strip())
    f.close()
print(li)
