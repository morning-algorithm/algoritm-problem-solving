n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    row, direct, cnt = map(int, input().split())
    row -= 1
    if direct == 0: #왼쪽으로 회전
        for i in range(cnt):
            '''mycode
            tmp = num[row][0]
            del num[row][0]
            num[row].append(tmp)'''
            num[row].append(num[row].pop(0))
    elif direct == 1: #오른쪽으로 회전
        for i in range(cnt):
            num[row].insert(0, num[row].pop())
            
            
result = 0
start = 0
last = n-1

for i in range(n):
    for j in range(start, last+1):
        result += num[i][j]
    if i < n//2:
        start += 1
        last -= 1
    else:
        start -= 1
        last += 1
    
print(result)
    
