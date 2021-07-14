from collections import deque

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

result = 0
weight = deque(weight)
'''my code
for i in range(n):
    for j in range(n-1, i, -1):
        if weight[i] + weight[j] <= m:
            weight[i] = 251
            weight[j] = 251
            result += 1
            break

for i in range(n-1, -1, -1):
    if weight[i] < 251:
        result += 1'''

while weight:
    if len(weight) == 1: #한 명이 남았다면 한 명만 태운다
        result += 1
        break
    elif weight[0] + weight[-1] > m: #제일 큰 값은 제일 작은 값이랑 짝이 되지 못 하면 혼자 타야함
        weight.pop()
        result += 1
    else:
        weight.popleft() #weight.pop(0)
        weight.pop()
        result += 1     
    
print(result)
