
import sys
sys.stdin = open("input.txt","rt")

#me 
'''정렬 기준 틀림!
n = int(input())
a= list()
for _ in range(n):
     tmp = tuple(map(int,input().split()))
     t = tmp[1] - tmp[0]
     a.append((t,tmp))
a.sort(key = lambda x : ( x[1][0],x[0]))
print(a)

e = a[0][1][1]
cnt = 1
for i in range(1,n):
    s = a[i][1][0]
    if s - e >= 0:
        print(s,e, a[i])
        e = a[i][1][1]
        cnt+=1
print(cnt)
'''

#answer
'''
* 그리디 알고리즘: 문제를 풀어나가는 과정에 있어서 현재 이 단계에서 가장 좋은 것이 뭔지 보고, 그것을 선택함
- 단계에서 가장 좋은것을 어떻게 판별?
- 거의 대부분의 그리디문제는 **정렬**을 한다음에 차례차례 선택하면 그리디가 된다.

* 풀이:
    - 누구를 기준으로 정렬하면 좋으냐? 
            - 회의가 끝나는 시간을 기준으로 정렬을 해야한다!! 회의가 빨리 끝나야 많이 할 수 있다.
            - 회의가 시작하는 시간으로 정렬을 하면안됨 ! 만약 일찍시작하고, 늦게 끝나면 회의를 많이 할 수 없다. 
    - 가장 빨리 끝나는 회의의 끝나는 시간을 기록해놓고,
    - 그다음에 빨리 끝나는 회의의 시작시간과 기록한 끝난 시간을 비교, 끝나는 시간보다 시작시간이 크거나 같으면 회의 가능.  
'''

n = int(input())
meeting = []
for i in range(n):
    s, e= map(int,input().split())
    meeting.append((s,e))
meeting.sort(key = lambda x : (x[1],x[0])) #끝나는 시간이 같으면 시작시간이 작은 것으로 정렬

et = 0
cnt = 0
for s,e in meeting:
    if s >= et: #첫번째회의는 무조건 참
        et = e
        cnt += 1
print(cnt)