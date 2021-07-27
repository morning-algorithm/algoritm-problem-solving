import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
mat = [[0]*(n) for _ in range(n)]

for i in range(m):
    n1, n2, p = map(int, input().split())
    mat[n1-1][n2-1] = p

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()
    
