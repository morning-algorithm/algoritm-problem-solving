import sys
#sys.stdin=open("input.txt", "r")

l = int(input())
boxList = list(map(int, input().split()))
m = int(input())

for i in range(m):
    maxIndex = boxList.index(max(boxList))
    minIndex = boxList.index(min(boxList))
    boxList[maxIndex] -= 1
    boxList[minIndex] += 1


ans = max(boxList) - min(boxList)
print(ans)
