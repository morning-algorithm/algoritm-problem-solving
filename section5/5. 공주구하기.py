import sys
#sys.stdin=open("input.txt", "r")
from collections import deque

n, k = map(int, input().split())
prince =list(range(1, n+1))
q = deque(prince)

while len(q) > 1:
    for i in range(1, k):
        q.append(q.popleft())
    q.popleft()

print(q.pop())    
