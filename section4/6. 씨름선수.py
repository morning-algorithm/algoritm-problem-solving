import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
info = []

for i in range(n):
    h, w = map(int, input().split())
    info.append((h, w))

info.sort(reverse=True)

largest = 0
count = 0

for h, w in info:
    if w > largest:
        largest = w
        count += 1
    
print(count)    
