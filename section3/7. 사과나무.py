import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
nList = [list()]*n

for i in range(n):
    nList[i] = list(map(int, input().split()))

sum = 0

s=e=n//2

for i in range(n):
    for j in range(s, e+1):
        sum += nList[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1


print(sum)
