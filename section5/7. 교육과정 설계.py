
import sys
from collections import deque
sys.stdin = open("input.txt","rt")

#me
''' queue에 넣는 대상이 잘못됨. 입력예제 2번을 커버하지 못함. 필수과목이 전부 설계과목에 들어가지 않았을 때를 체크안함.
a = list(input()) #우선순위 높을 수록 숫자 작다
n = int(input())

for N in range(n):
    b = list(input())

    for i in range(len(b)):
        if b[i] in a:
            b[i] = (a.index(b[i]),b[i])

    must = deque(filter(lambda x: type(x) == tuple, b))
    r = True

    while must and r:
        current = must.popleft()
        
        for i in range(len(must)):
            if must[i][0] == current[0]:
                must[i] = (99,must[i][1])
            elif must[i][0] < current[0]:
                r = False


    if r:
        print(f"#{N+1} YES")
    else:
        print(f"#{N+1} NO")
'''

#answer
'''
queue에 넣는 대상은 필수과목.
리스트를 순회하며 필수과목이면 queue를 pop하여 일치하면 넘어감, 일치하지 않으면 실패
그리고 queue엔 아무것도 남아있지 않아야함 -> 필수과목이 전부 들어가야하므로
매 리스트마다 queue초기화.
'''
a = list(input()) #우선순위 높을 수록 숫자 작다
n = int(input())

for N in range(n):
    b = list(input())
    dq = deque(a)

    for i in b:
        if i in dq and dq.popleft() != i: #입력예제 2번도 커버됨
            print(f"#{N+1} NO")
            break
    else:
        if dq:
            print(f"#{N+1} NO")
        else:
            print(f"#{N+1} YES") 
            


        