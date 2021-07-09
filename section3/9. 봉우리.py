n = int(input())
num = num = [list(map(int, input().split())) for _ in range(n)]
result = 0

'''mycode
direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

for i in range(n):
    for j in range(n):
        isMax = True
        cur = num[i][j]
        for z in range(4):
            x = i + direct[z][0]
            y = j + direct[z][1]
            if 0<=x<n and 0<=y<n and cur <= num[x][y]:
                isMax = False
        
        if isMax:
            result += 1
'''
num.insert(0, [0]*n)
num.append([0]*n)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for x in num:
    x.insert(0, 0)
    x.append(0)
               
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(num[i][j] > num[i+dx[k]][j+dy[k]] for k in range(4)):
            result += 1

print(result)
