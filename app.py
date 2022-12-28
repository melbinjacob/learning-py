students = [
    "Arun",
    "Barun",
    "Carun",
    "Darun",
]

s1 = [
    10,
    11,
    12,
    13
]
s2 = [
    20,
    21,
    22,
    23
]
s3 = [
    30,
    31,
    32,
    33
]

student = input("What is your name: ")
if student in students:
    sutPos = students.index(student)
    for i in s1, s2, s3:
        sum = s1[sutPos] + s2[sutPos] + s3[sutPos]
    print(student + " your total marks is " + str(sum))
else:
    print("Student not found!")
