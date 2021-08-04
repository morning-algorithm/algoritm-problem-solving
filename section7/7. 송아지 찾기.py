import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#me
'''
dfs 중복순열로 구하면 어떨까 생각함.
처음 14가 나오는 순간의 레벨을 기록하고, 그 레벨을 넘어가면 가지치기 하는 식으로
'''

#answer
'''
BFS
- 넓이(레벨) 우선 탐색

- **최단 거리**를 구할때 사용한다!
    - 왜냐? 쭈욱 레벨 우선 탐색하다가 루트노드랑 제일 가까운 레벨에서 나오는 답이 최단거리다!
    - 그 이후 레벨은 최단거리가 아니므로 더이상 볼 필요가 없으므로 바로 break한다. 
    - ex) 한번만에 가는 곳 다 탐색했는데 없어요. 두번만에 다 가는 곳 탐색했는데 또 없어요. 세번만에 가는 곳 탐색했는데 있어요 ! => 세번이최단거리. 이 순간 종착점.

- **deque()**를 이용.
    - queue에 start 값 넣은다음에.
    - while queue: 를 이용 !!!! bfs는 queue가 비면 멈춘다.!! (dfs처럼 재귀 호출(스택 활용 위함) 이용하는 것 아님)
    - queue애서 popleft()한다음에
    - 뽑은 값의 자식들을 큐에 넣는데, 이때 중복 체크를 통해 갔던 곳 또 안가게 한다.

'''

s,e = map(int,input().split())
d = [5,1,-1]
ch = [0] * 10001
dis = [0] * 10001
q = deque()
q.append(s)
dis[s] = 0
ch[s] = 1

while q:
    now = q.popleft()
    if e == now:
        print(dis[now])
        sys.exit(0)
    
    for item in d:
        next = now + item
        if 0 < now + item <= 10000 and ch[next] == 0:
            ch[next] = 1
            dis[next] = dis[now] + 1
            q.append(next)
            
    # bfs(q.popleft()) <- 재귀호출 이용 아니다.

                          
