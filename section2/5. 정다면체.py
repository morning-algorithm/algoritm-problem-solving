import sys
#sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
sumList = [0]*(n+m+3)

for i in range(1, n+1):
    for j in range(1, m+1):
        sumList[i+j] += 1

max = sumList[0]
for i in range(1, len(sumList)):
    if max < sumList[i]:
        max = sumList[i]

for i in range(len(sumList)):
    if max == sumList[i]:
        print(i, end=' ')
    
    
        
    
