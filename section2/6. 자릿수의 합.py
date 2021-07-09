def digit_sum(x):
    x = str(x)
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    return sum

n = int(input())
num = list(map(int, input().split()))
           
max = 0
maxNum = 0
for x in num:
    sum = digit_sum(x)
    if sum > max:
        max = sum
        maxNum = x
        
print(maxNum)
