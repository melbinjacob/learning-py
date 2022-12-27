sum_even = 0
sum_odd = 0
for i in range (1,51,2):
    sum_even += i
    sum_odd += i+1
print("Sum of even = " + str(sum_even))
print("Sum of odd = " + str(sum_odd))
