import sys
#sys.stdin=open("input.txt", "rt")

n,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

cnt=0

while True:
    i=0
    j=n-1
    if n>0:
        if i==j:
            cnt+=1
            break
        if a[i]+a[j]<=k:
            cnt+=1
            a.pop(i)
            a.pop(j-1)
            n-=2
        else:
            cnt+=1
            a.pop(j)
            n-=1
    else:
        break

print(cnt)