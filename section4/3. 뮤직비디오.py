import sys
#sys.stdin=open("input.txt", "r")

def Count(capacity):
    cnt=1
    sum=0
    for x in pList:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m = map (int, input().split())
pList = list(map(int, input().split()))
maxx = max(pList)

s = 1
e = sum(pList)
ans = 0
while s <= e:
    mid=(s+e)//2
    if mid >= maxx and Count(mid) <= m:
        ans = mid
        e = mid-1
    else:
        s =mid+1
        
print(ans)

