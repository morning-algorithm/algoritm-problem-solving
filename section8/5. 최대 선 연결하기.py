import sys
#sys.stdin = open("input.txt","r")

n = int(input())
arr=list(map(int, input().split()))

dy = [0]*n
dy[0]=1
res=0

for i in range(1,n):
    m=0
    for j in range(i-1, -1,-1):
        dy[i]=1
        if arr[j]<arr[i] and dy[j]>m:
            m=dy[j]
    dy[i]=m+1

print(max(dy))

