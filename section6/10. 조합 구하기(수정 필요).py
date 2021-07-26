import sys
#sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())

for i in  range(1, n):
    for j in range(i+1, n+1):
        print(i, j)
