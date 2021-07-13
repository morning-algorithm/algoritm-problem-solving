n = int(input())
map = list(map(int, input().split()))
m = int(input())

map.sort()

for _ in range(m):
    map[0] += 1
    map[n-1] -= 1
    map.sort()

print(map[n-1] - map[0])
