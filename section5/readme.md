section 5. data structure (stack, queue, hash, heap)

**[스택]** - LIFO

**[큐]** - FIFO, 파이썬 라이브러리 deque 활용

from collections import deque

dq=list()
dq=deque(dq)

dq.appendleft(1) #맨 앞에 원소 삽입
dq.popleft() #맨 앞의 원소 제거

dq.append(1) # 맨 뒤에 원소 삽입
dq.popleft() # 맨 뒤의 원소 제거



* tuple
a=list(range(11,20))
t=[(position, value) for position, value in enumerate(a)]
#[(0,11),(1,12), ... ,(7,18),(8,19)]

*dictionary
 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합
