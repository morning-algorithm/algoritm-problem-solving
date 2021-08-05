import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#me
'''
상하좌우를 -1로 wrap하니까 편헀음.
처음엔 레벨로 생각해서 아 레벨이 6일때까지만 해야겠다고 했는데 갈수 있는 땅이 따로 있기때문에 이건 통하지않았음.
큐가 비어있지 않은 동안 while문 돌아서. 
'''
a = [ list(map(int,input().split())) for _ in range(7) ]
for item in a:
      item.insert(0,-1)
      item.append(-1)
a.insert(0,[-1]*9)
a.append([-1]*9)

dx = [ -1, 0, 1, 0]
dy = [0, 1, 0, -1]
ch = [ [0]*9 for _ in range(9) ]
dis = [ [0]*9 for _ in range(9) ]

q = deque()
q.append((1,1))

while q:
      now = q.popleft()
      
      if now[0] == 7 and now[1] == 7:
            print(dis[now[0]][now[1]])
            sys.exit(0)
      
      for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]

            if a[x][y] == 0 and ch[x][y] == 0: #answer: 이때 간단하게 0<=x<=6 그리고 0<=y<=6일때만 배열 접근하도록 하면 -1 wrapping안해도 됨.
                  ch[x][y] = 1 #answer: ch사용하는 대신에 a값 자체를 1(벽)으로 만들어버려도됨.
                  dis[x][y] = dis[now[0]][now[1]] + 1
                  q.append((x,y))
print(-1)

#answer
'''
자식은 부모의 상하좌우.
dis 사용. 부모의 dis + 1씩해나간다.
한번 간 지점은 체크해서 다시 가면안된다.
]간단하게 0<=x<=6 그리고 0<=y<=6일때만 배열 접근하도록 하면 -1 wrapping안해도 됨.
ch사용하는 대신에 a값 자체를 1(벽)으로 만들어버려도됨.
while q끝난다음에 dis가 0이면 도착하지 못한것이므로 -1출력.
'''
