li = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    13
]


sumOdd = 0
for i in li:
    if i % 2 == 1:
        sumOdd += i
print(sumOdd)

i = 0
sum2 = 0
while i < len(li):
    if li[i] % 2 == 1:
        sum2+=li[i]
    i += 1
print(sum2)
