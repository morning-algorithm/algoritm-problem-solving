import sys
#sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))

def count(len):
    cnt=0
    for x in a:
        cnt+=int(x//len)
    return cnt

a.sort()
lt=0
rt=a[n-1]
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)>=k:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)