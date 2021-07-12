import sys
#sys.stdin = open("input.txt","rt")

#me
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

s = 0
e = n-1
mid = (s+e) // 2 

while a[mid] != m:
    if m < a[mid]:
        e = mid - 1
        mid = (s+e) // 2 
    elif m > a[mid]:
        s = mid + 1
        mid = (s+e) // 2 
    else:
        break   

print(mid+1)

#answer
'''
이분검색은 log2 n 의 시간복잡도
while s<=e
'''