import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
nList = [list()] * n

for i in range(n):
    nList[i] = list(map(int, input().split()))
    
maxSum = 0
sum = 0

for i in range(n):
    sum = 0
    for j in range(n):
            sum += nList[i][j]
    if sum > maxSum:
        maxSum = sum

for i in range(n):
    sum = 0
    for j in range(n):
            sum += nList[j][i]
    if sum > maxSum:
        maxSum = sum

for i in range(n):
    sum = 0
    for j in range(n):
            sum += nList[j][j]
    if sum > maxSum:
        maxSum = sum

for i in range(n):
    sum =0
    for j in range(n):
        sum += nList[i][n-1-j]
    if sum > maxSum:
        maxSum = sum

print(maxSum)
