import sys
sys.stdin=open("input.txt", "rt")

s=list(input())
n=int(input())
t=[]

for i in range(n):
    arr=list(input())
    for j in range(len(arr)):
        if arr[i] in s:
            arr.pop()

'''
# 오답 : CEDF일 때, CEFDF이어도 YES로 처리함. 순서를 반드시 유지하고 입력된 과목의 순서가 틀리면 안됨.
for i in range(n):
    t.clear()
    t=list(s) # 배열 깊은 복사하기 cf) t=s-> 얕은 복사
    arr=list(input())
    while arr and t:
        if arr[0]==t[0] :
            t.pop(0)
        arr.pop(0)
    if len(t)==0:
        print("#", end="")
        print(i+1, end=" ")
        print("YES")
    else:
        print("#", end="")
        print(i+1, end=" ")
        print("NO")
'''

'''정답
from collections import deque
need=input()
n=int(input())

for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft()
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
'''
