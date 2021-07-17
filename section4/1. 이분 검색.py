import sys
#sys.stdin=open("input.txt", "rt")

n,m = map(int, input().split())
a=list(map(int, input().split()))

a.sort()

lt=0
rt=n-1
loc=-1

while True:
    mid=(lt+rt)//2
    if a[mid]==m:
        loc=mid
        break
    elif a[mid]<m:
        lt=mid+1
    elif a[mid>m]:
        rt=mid-1

print(loc+1)