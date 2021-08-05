
def DFS(x, y):
    global count
    if x == 6 and y == 6:
        count += 1
    else:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a <= 6 and 0 <= b <= 6 and board[a][b]!= 1:
                board[a][b] = 1
                DFS(a, b)
                board[a][b] = 0

board = [list()] * 7
for i in range(7):
    board[i] = list(map(int, input().split()))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0

board[0][0] = 1 #출발점
DFS(0, 0)
print(count)
