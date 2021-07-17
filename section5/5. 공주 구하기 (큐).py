import sys
from collections import deque
sys.stdin=open("input.txt", "rt")

n,k = map(int, input().split())
arr = [i for i in range(1,n+1)]
q=deque(arr)
cnt=1

while len(q)>1:
    p=q.popleft()#맨 앞 원소 꺼내기
    if cnt!=k:#k를 외치지 않았다면 다시 줄 서기
        q.append(p)
        cnt+=1
    else:#k를 외쳤다면 1부터 다시시작
        cnt=1


for a in q:
    print(a)

'''정답풀이
n,k=map(int, input().split())
dq=list(range(1,n+1))
dq=deque(dq)
while dq:
    for _ in range(k-1):#k-1까지의 사람을 popleft 후 뒤에 줄서기 append()
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()#k 외친 사람 제거
    if len(dq)==1:#마지막 사람 출력
        print(dq[0])
        dq.popleft()#dq 비우기
'''