n, m = map(int, input().split())
dy=[0]*(m+1)

for i in range(n):
    weight, value = map(int, input().split())
    for j in range(weight, m+1):
            dy[j]=max(dy[j], dy[j-weight]+value)
print(dy[m])

