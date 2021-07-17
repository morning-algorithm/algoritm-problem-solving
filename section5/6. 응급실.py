import sys
from collections import deque
#sys.stdin=open("input.txt", "rt")

n,k = map(int, input().split())
dq = deque(list(map(int, input().split())))# 위험도 큐
nq = deque(list(range(n))) # 위험도를 가진 사람의 고유번호 큐
order=0

while dq:
    cur=dq.popleft()
    curp=nq.popleft()
    if max(dq)<=cur:# 위험도 높은 사람이 없음
        order+=1 
        if curp==k:
            print(order)
            break
    else:
        dq.append(cur)
        nq.append(curp)


'''정답풀이
n,m=map(int, input().split())
# tuple 자료형으로 위험도와 index를 저장
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))] 
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):#위험도가 높은 사람이 한 사람이라도 있으면
        Q.append()
    else:
        cnt+=1
        if cur[0]==m:
            break

'''