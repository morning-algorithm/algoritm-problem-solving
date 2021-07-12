n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]

result = 0
start = last = n//2

for i in range(n):
    for j in range(start, last+1):
        result += num[i][j]
    if i < n//2:
        start -= 1
        last += 1
    else:
        start += 1
        last -= 1

print(result)
