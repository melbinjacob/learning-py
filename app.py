dict = {
    "brand" : "Ford",
    "model" : "Musthang",
    "Year"  : 1989
}

dict["Color"] = "blue"
dict.popitem()
del dict["brand"]
dict.clear()
del dict
print(dict)