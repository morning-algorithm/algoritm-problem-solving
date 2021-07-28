import sys
#sys.stdin=open("input.txt", "r")

def DFS(idx, sum):
    if idx == k:
        if 0 < sum <= s:
            sList.add(sum)
    else:
        DFS(idx+1, sum+kList[idx])
        DFS(idx+1, sum-kList[idx])
        DFS(idx+1, sum)


k = int(input())
kList = list(map(int,input().split()))

s = sum(kList)
sList = set()

DFS(0, 0)

count = s - len(sList)
print(count)



