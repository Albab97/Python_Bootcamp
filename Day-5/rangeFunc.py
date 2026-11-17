# Range function with For Loop : range(1,10) --> 1 to 9 (10 not included)
for number in range(1,10):  
    print(number)

for number in range(1,11,3):
    print(number)

sum = 0
for num in range(1,101):
    sum+=num
print(sum)