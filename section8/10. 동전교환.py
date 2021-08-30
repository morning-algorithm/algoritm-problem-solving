n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy=[100]*(m+1)
dy[0] = 0

for i in range(n):
    p = coin[i]
    for j in range(p, m+1):
            dy[j]=min(dy[j], dy[j-p] + 1)
print(dy[m])
