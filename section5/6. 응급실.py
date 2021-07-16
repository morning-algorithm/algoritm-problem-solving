from collections import deque

n, m = map(int, input().split())
'''num = list(map(int, input().split()))
my code
order = []
for i in range(n):
    order.append(i)

q = deque(order)
cnt = 0

while True:
    index = q.popleft()
    if max(num) == num[index]:
        num[index] = -1
        cnt += 1
        if index == m:
            print(cnt)
            break            
    else:
        q.append(index)'''
        
q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
q = deque(q)
cnt = 0
while True:
    cur = q.popleft()
    if any(cur[1] < x[1] for x in q): #위험도가 더 높은 사람이 있다
        q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
        
