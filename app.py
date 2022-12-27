sum_even = 0

li_odd = []
li_even = []

for i in range (1,51,2):
    
    sum_even += i
    li_even.append(i)
    li_odd.append(i+1)

print(li_even)
print(li_odd)
