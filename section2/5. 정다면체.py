n, m = map(int, input().split())
sumCount = [0] * (n+m+1) #index는 0부터 n+m까지

maxCount = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        sumCount[i+j] += 1
        if sumCount[i+j] > maxCount:
            maxCount = sumCount[i+j]

for idx, x in enumerate(sumCount):
    if x == maxCount:
        print(idx, end=' ')
            
