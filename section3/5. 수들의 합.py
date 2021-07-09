n, m = map(int, input().split())
num = list(map(int, input().split()))

sum = num[0]
result = 0
start = 0
last = 1

while True:
    if sum < m:
        if last < n:
            sum += num[last]
            last += 1
        else:
            break
    elif sum == m:
        result += 1
        sum -= num[start]
        start += 1
    else:
        sum -= num[start]
        start += 1

print(result)
