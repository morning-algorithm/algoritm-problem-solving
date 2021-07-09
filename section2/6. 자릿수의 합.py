import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
numList = list(map(int, input().split()))
sumList = [0]*n

def digit_sum(x):
    sum = 0

    while x > 0:
        sum += x%10
        x = x/10
        
    return sum

for i in range(n):
    sumList[i] = digit_sum(numList[i])

max = sumList[0]
index = 0
for i in range(1, n):
    if max < sumList[i]:
        max = sumList[i]
        index = i
        
print(numList[i])