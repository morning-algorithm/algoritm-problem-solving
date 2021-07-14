import sys
#sys.stdin = open("input.txt","rt")

#me
n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
b = 0
while n>1:
    for i in range(1,n):
        if a[0]+a[n-i] <= m:
            a.pop(n-i)
            a.pop(0)
            n-=2
            b+=1
            a.sort()
            break
    else: 
        a.pop(0)
        n-=1
        b+=1
if n == 1:
    b+=1

print(b)

#answer
'''
* 풀이: 
먼저,승객의 몸무게를 오름차순 정렬
몸무게 가장 작은 사람과 가장 큰사람이 보트에 함께 탈수 있는지 확인
- 같이 탈 수 없으면? 
        - !!!!!제일 큰 사람은 혼자 타고 가야하므로 pop!!!!!! (제일 작은 사람과 탈 수 없다면 누구와도 탈 수 없다.,  
        - 그리고 나서 제일 마지막 사람과 다시 같이 타고 갈 수 있는지검색.
- 같이 탈 수 있으면?
        - 맨 앞사람, 맨 뒷사람 둘다 pop
- 마지막에 한명에 남을 경우? 위 로직만으론 오류가남. len(p) == 1 일때는 그냥 보트에 태워 보내기.

* 더 효율적인 방법:
리스트의 pop(0)은, 앞으로 한칸 씩 옮겨야 하므로 비효율적임.(like 배열)
deque 자료구조는 앞에서도, 뒤에서도 넣었다 뺄 다 할 수 있는데 단순히 포인터를 이용하므로 더 효율적임. 땡기는 연산 x

from collections import deque
deque(리스트)

p.popleft() # 더 효율적 !!
p.pop()
'''