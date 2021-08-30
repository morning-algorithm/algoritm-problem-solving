n = int(input())
nList = list()

for i in range(n):
    nList.append(list(map(int, input().split())))

dy=[[0]*n for _ in range(n)]
dy[0][0] = nList[0][0]

for i in range(n): #가장자리
    dy[0][i] = dy[0][i-1] + nList[0][i]
    dy[i][0] = dy[i-1][0] + nList[i][0]

for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + nList[i][j]

print(dy[n-1][n-1])
