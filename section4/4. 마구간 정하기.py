import sys
#sys.stdin=open("input.txt", "r")

def Count(len):
    c = 0
    p=nList[0]
    for i in range(1, n):
        if nList[i]-p >= len:
            c += 1
            p = nList[i]
    return c


n, c = map(int, input().split())
nList = []

for i in range(n):
    nList.append(int(input()))

nList.sort()

s = 1
e = nList[n-1]
short = e

while s <= e:
    mid=(s+e)//2
    if Count(mid)>=c:
        short=mid
        lt=mid+1
    else:
        rt=mid-1
        
print(short)
        



