
import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#me
'''큐에 전부 넣어놓고 시작해야된다는 것 생각하기!''' 
n,k = map(int,input().split())
cnt = 0
q = deque(list(range(1,n+1)))

while n>1:
    cnt += 1
    if cnt != k:
        q.append(q.popleft())
    else: 
        q.popleft()
        n -= 1
        cnt = 0

print(q.popleft())
    

#answer
'''
* Queue
    - FIFO, 들어가는 순서대로 나온다
    - append(), popleft() / appendleft(), pop()
* 풀이:
    큐에 전부 넣어놓고!! 
    큐에 한사람만 남을 때까지
        맨 앞 사람이 번호 외치고 
         - k랑 같지 않으면 뽑아서 뒤에 다시 넣기
         - k랑 같으면 그냥 뽑기
        => 원형으로 도는 것 같은 논리가 됨,
'''