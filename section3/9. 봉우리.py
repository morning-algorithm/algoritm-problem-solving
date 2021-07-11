import sys
#sys.stdin=open("input.txt", "rt")

n=int(input())

a=[[0 for col in range(n+2)]for row in range(n+2)]

for i in range(1,n+1):
    a[i][1:n+1]=list(map(int, input().split()))

cnt=0
for i in range(1, n+1):
    for j in range(1,n+1):
        if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1]:
            cnt+=1
print(cnt)