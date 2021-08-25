n = int(input())
nList = list(map(int, input().split()))
nList.insert(0,0)
dy = [0] * (n+1)
dy[1] = 1
count = 0
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if nList[j] < nList[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max+1
    if dy[i] > count:
        count = dy[i]
print(count)



'''
n = int(input())
nList = list(map(int, input().split()))

len = 0

for i in range(n):
    count = 1
    a = nList[i]
    for j in range(i+1, n):
        if a < nList[j]:
            print(nList[j], end = '')
            count += 1
            a = nList[j]
    if count > len:
        len = count
    print()

print(len)
'''
