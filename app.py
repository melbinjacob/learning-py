sum_even = 0
sum_odd = 0
for i in range (1,51):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("Sum of even = " + str(sum_even))
print("Sum of odd = " + str(sum_odd))
