def count(line_len):
    cnt = 0
    for x in line:
        cnt += (x // line_len)

    return cnt

k, n = map(int, input().split())
line = []
result = 0
largest = 0

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (rt + lt) // 2
    if count(mid) >= n:
        result = mid
        lt = mid + 1 #최대 길이 구하는 거니까 더 좋은 답 찾기 위해 더 검
    else: #너무 길다
        rt = mid-1

print(result)
