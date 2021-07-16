from collections import deque
n, k = map(int, input().split())
prince = list(range(1,n+1))
q = deque(prince)

while q:
    for _ in range(k-1):
        x = q.popleft()
        q.append(x)
    q.popleft()

    if len(q) == 1:
        print(q.pop())
