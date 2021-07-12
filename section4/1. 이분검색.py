import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
numList = list(map(int, input().split()))

numList.sort()

"""
for i in range(n):
    if numList[i] == m:
        print(i+1)
        break;
"""

s = 0
e = n-1

while s <= e:
    mid = (s+e)//2
    if m < numList[mid]:
        e = mid
    elif m > numList[mid]:
        s = mid
    elif m == numList[mid]:
        print(mid+1)
        break;
        
