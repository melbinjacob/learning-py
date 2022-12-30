abc = "python is a simple programming language"
words = abc.split(" ")
print(words)
print(len(words))
for i in words:
    print(i + " >" + str(len(i)))