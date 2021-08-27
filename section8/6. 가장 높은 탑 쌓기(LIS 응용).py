n = int(input())
brick = []

for i in range(n):
    area, height, weight = map(int, input().split())
    brick.append((area, height, weight))

brick.sort(reverse = True)

dy = [0]*n
dy[0] = brick[0][1]
h = brick[0][1];

for i in range(1, n):
    max = 0;
    for j in range(i-1, -1, -1):
        if brick[j][2] > brick[i][2] and dy[j] > max:
            max = dy[j]
    dy[i] = max + brick[i][1]
    
    if h < dy[i]:
        h = dy[i]
    
print(h)
    
'''
n = int(input())
brick = []

for i in range(n):
    area, height, weight = map(int, input().split())
    brick.append((area, height, weight))

brick.sort(reverse = True)
brick.append((0, 0, 0))
print(brick)

h = brick[0][1]
a = 0
max = 0

for j in range(n):
    h = brick[j][1]
    a = j
    for i in range(j+1, n):
        print(j, i)
        if brick[i][2] <= brick[a][2]:
            a = i
            h += brick[i][1]
            print(brick[i][1])
    if max < h:
        max = h

print(max)

'''
