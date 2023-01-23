set = {
    "blue",
    "green",
    "red",
    "black"
}

for x in set:
    print(x)

if "white" in set:
    print("Yes white is in this set")
else:
    print("No")

set.add("yellow")
print(set)

x = {1,2,3}
set.update(x)
print(set)

set.remove("blue")
print(set)

set.clear()
print(set)
