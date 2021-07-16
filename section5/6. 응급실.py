import sys
from collections import deque
sys.stdin = open("input.txt","rt")

#me
'''enumerate힌트얻음! 몇번째 환자인지 판별할 수 있게 됨.
처음엔 60 60 90 60 60 60의 경우에 단순히 값으로만 비교하여 몇번째환자인지 판별하지 못했었음.'''
n,m = map(int,input().split())
a = list(enumerate(map(int,input().split())))
dq = deque(a)

cnt = 0
while True:
    h = dq.popleft()
    for item in dq:
        if item[1] > h[1]:
           dq.append(h)
           break
    else:
        cnt+=1
        if h[0] == m:
            break
print(cnt)

#answer
'''
문제있는대로 시뮬레이션 해야함 !
60 60 90 60 60 60 때문에 정렬하면 안됨. 

* enumerate
    - 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
    - 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
* any()
    - any(cur[1] < x[1] for x in Q): for문 돌면서 단 한개라도 참인게 있으면 참이됨 !
    '''