import sys
#sys.stdin=open("input.txt", "r")

def DFS(deg, s):
    global count
    if deg == k:
        if sum(tmp)%m == 0:
            count += 1
    else:
        for i in range(s, n):
            tmp[deg] = nList[i]
            DFS(deg+1, i+1)



n, k = map(int, input().split())
nList = list(map(int, input().split()))
m = int(input())

tmp = [0]*k
count = 0

DFS(0, 0)

print(count)
