mo_conv = {
        "Jan" : "January",
        "Feb" : "February",
        "Mar" : "March",
        "Apr" : "April",
        "May" : "May",
        "Jun" : "June",
        "Aug" : "August",
        "Sep" : "September",
        "oct" : "October",
        "Nov" : "November",
        "Dec" : "December"
}

print(mo_conv["Dec"])
print(mo_conv.get("Dec"))
print(mo_conv.get("Lov", "Not a valid key"))

nu_conv = {
        1 : 10,
        2 : 20,
        3 : 30,
        4 : 40,
        5 : 50,
        6 : 60,
        7 : 70,
        8 : 80,
        9 : 90,
        10 : 100
}

#you can store any type of key value pairs in dict
rand = {
        1 : True,
        "True" : False,
        False : 3.4,
}