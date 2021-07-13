def count(distance):
    beforePosition = position[0]
    cnt = 1
    for x in range(1, n):
        currentPosition = position[x]
        if currentPosition - beforePosition >= distance:
            cnt += 1
            beforePosition = currentPosition
    
    return cnt
    
n, c = map(int, input().split())
position = []
for i in range(n):
    position.append(int(input()))
position.sort()
lt = position[0]
rt = max(position)
result = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:
        result = mid
        lt = mid+1
    else:
        rt = mid-1

print(result)
