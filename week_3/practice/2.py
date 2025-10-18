#  given a number do the sum of all the digits

num = 5678935678

sum = 0
for i in str(num):
    sum += int(i)

print(sum)
