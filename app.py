len1 = 4
len2 = 5
len3 = 3


if len1 > len2 and len1 > len3:
    if len1 * len1 == len2*len2 + len3*len3:
        print("Square triangle")
    else:
        print("Not a square triangle")
elif len2 > len3:
    if len2 * len2 == len1*len1 + len3*len3:
        print("Square triangle")
    else:
        print("Not a square triangle")
else:
    if len3 * len3 == len2*len2 + len1*len1:
        print("Square triangle")
    else:
        print("Not a square triangle")
