import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
nList = [list()] * n

for i in range(n):
    nList[i] = list(map(int, input().split()))

nList.insert(0, [0]*n)
nList.append([0]*n)
for i in range(len(nList)):
    nList[i].insert(0, 0)
    nList[i].append(0)

count = 0
for i in range(1, len(nList)):
    for j in range(1, len(nList)):
        tmp = nList[i][j]

        if tmp > nList[i][j-1] and tmp > nList[i][j+1] and tmp > nList[i-1][j] and tmp > nList[i+1][j]:
            count += 1

print(count)
