import sys
#sys.stdin=open("input.txt", "r")


def Count(length):
    cnt=0
    for x in kList:
        cnt+=(x//length)
    return cnt

k, n = map(int, input().split())
kList = [0]*k
long = 0

for i in range(k):
    kList[i] = int(input())
    long = max(kList[i], long)

s = 0
ans = 0

while s <= long:
    mid = (s+long)//2
    if Count(mid) >= n:
        ans = mid
        s = mid+1
    else:
        long = mid-1
    
print(ans)







