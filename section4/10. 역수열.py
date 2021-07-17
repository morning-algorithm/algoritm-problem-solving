import sys
#sys.stdin=open("input.txt", "rt")

n= int(input())
a = list(map(int,input().split()))
res=[0]*n
loc=[i for i in range(n)]

for i in range(n):
    res[loc[a[i]]]=i+1
    loc.pop(a[i])

for x in res:
    print(x,end=" ")