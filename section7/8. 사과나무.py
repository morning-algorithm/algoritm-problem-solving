import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#answer
'''
격자판은 시계방향으로 탐색
그런데 dfs를 곁들여서.
시작점은 격자의 정 가운데. 이곳이 레벨 0
레벨이 (격자판//2) 되면 queue에 그만 추가해야하니까 break.
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
L = 0

s = (n//2, n//2)
q = deque()
q.append(s)
sum = 0

while True:
    if n//2 == L : #start 가 L:0, 그다음이 L:1인데, L1 의 자식 시계방향들까지만 보면 원하는 탐색 끝이므로.
        break 
    for _ in range(len(q)): #L0: 원소 하나이므로 한번만 자식들 넣으면되고, L1은 원소 4개 이므로 4번 자식들을 넣으면됨
        tmp = q.popleft()
        for i in range(4):
            x = tmp[0]+dx[i]
            y = tmp[1]+dy[i]
            if ch[x][y] == 0:
                ch[x][y] = 1
                sum += a[x][y]
                q.append((x,y))
    L+=1

print(sum)
