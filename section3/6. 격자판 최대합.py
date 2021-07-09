n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
max = 0
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += num[i][j] #행의 합
        sum2 += num[j][i] #열의 합
    if sum1 > max:
        max = sum1
    if sum2 > max:
        max = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += num[i][i]
    sum2 += num[i][n-i-1]

if sum1 > max:
    max = sum1
if sum2 > max:
    max = sum2

print(max)
