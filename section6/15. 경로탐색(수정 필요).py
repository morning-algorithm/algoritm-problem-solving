import sys
#sys.stdin=open("input.txt", "r")


def DFS(level, ch):
    print(level)
    global count
    if level == n-1:
        count += 1
    else:
        for i in range(n):
            if mat[level][i] == 1:
                ch[level] += 1 
                if ch[i] != 1:
                    DFS(i, level)
                ch[level] = 0


n, m = map(int, input().split())
mat = [[0]*(n) for _ in range(n)]
count = 0
ch = [0]*n

for i in range(m):
    n1, n2 = map(int, input().split())
    mat[n1-1][n2-1] = 1

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()

DFS(0, 0)
print(count)
