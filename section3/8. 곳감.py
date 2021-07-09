import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
nList = [list()] * n

for i in range(n):
    nList[i] = list(map(int, input().split()))

command = int(input())

for i in range(command):
    row, dir, num = map(int, input().split())

    if dir == 0:
        for j in range(num):
            change = nList[row-1].pop(0)
            nList[row-1].append(change)
    elif dir == 1:
        for j in range(num):
            change = nList[row-1].pop()
            nList[row-1].insert(0, change)
    
s = 0
e = n-1
sum = 0

for i in range(n):
    for j in range(s, e+1):
        sum += nList[i][j]
        
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(sum)
