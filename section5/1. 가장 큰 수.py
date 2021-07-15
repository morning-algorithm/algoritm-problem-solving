
import sys
#sys.stdin = open("input.txt","rt")

#me
'''재귀&자식 을 이용해서 접근하려함'''

#answer
'''
* stack
    - LIFO : 나중에 들어온 것이 먼저 나온다
    - 구덩이
    - python list의 pop(), append()

* 풀이:
    - 지우기 cnt 남았으면 && 자기보다 작으면 계속 pop
    - 그리고 append 
    - for문이 전부 끝났는데 cnt가 남았으면? slice사용해 남은 cnt만큼 스택 뒤에 잘라냄!

* 팁:
    숫자 리스트를 for문 안돌고 한번에 출력하려면
    ''.join(map(str,숫자리스트))
'''
a,m = input().split()
a = list(map(int,list(a)))
m = int(m)

s = [a[0]]


for i in range(1,len(a)):
    while m > 0 and len(s) > 0 and s[-1] < a[i]:
        s.pop()
        m-=1
    s.append(a[i])


if m>0:
    s = s[:-m]

for item in s:
    print(item, end = '')

    